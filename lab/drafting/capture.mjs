// Privacy check, run before any real call: a stand-in for the DeepSeek API on 127.0.0.1
// inside the container. It answers every request with a short successful Messages stream, so
// dsh finishes a whole turn (task and session title) and every request it would send is seen.
// For each request it records the top-level fields, and LEAK with the name of either extra
// found anywhere in the raw body, nested or not. run_dsh.ps1 points DEEPSEEK_BASE_URL here
// with a fake key, and fails on any LEAK or on a turn that did not complete.
import { createServer } from 'node:http'
import { appendFileSync } from 'node:fs'
import { brotliDecompressSync, gunzipSync, inflateSync } from 'node:zlib'

const events = [
  ['message_start', { type: 'message_start', message: { id: 'msg_capture', type: 'message', role: 'assistant', model: 'capture', content: [], stop_reason: null, stop_sequence: null, usage: { input_tokens: 1, output_tokens: 0 } } }],
  ['content_block_start', { type: 'content_block_start', index: 0, content_block: { type: 'text', text: '' } }],
  ['content_block_delta', { type: 'content_block_delta', index: 0, delta: { type: 'text_delta', text: 'ok' } }],
  ['content_block_stop', { type: 'content_block_stop', index: 0 }],
  ['message_delta', { type: 'message_delta', delta: { stop_reason: 'end_turn', stop_sequence: null }, usage: { output_tokens: 1 } }],
  ['message_stop', { type: 'message_stop' }],
]

createServer((req, res) => {
  const chunks = []
  req.on('data', (c) => { chunks.push(c) })
  req.on('end', () => {
    // A compressed body is read decompressed; one that cannot be read is UNREADABLE, and
    // run_dsh.ps1 fails on that as on a LEAK - never read as clean.
    let body
    try {
      const raw = Buffer.concat(chunks)
      const enc = (req.headers['content-encoding'] || 'identity').toLowerCase()
      const bytes = enc === 'gzip' ? gunzipSync(raw) : enc === 'deflate' ? inflateSync(raw)
        : enc === 'br' ? brotliDecompressSync(raw) : enc === 'identity' ? raw : null
      body = bytes === null ? null : bytes.toString('utf8')
    } catch { body = null }
    const extras = ['dsh_session_log', 'dsh_plugin_packages']
    // Raw text, and every key of the decoded JSON at any depth: an escaped key such as
    // "dsh_session_log" decodes to the same field without matching the raw text.
    const leaks = new Set(body === null ? [] : extras.filter((f) => body.includes(f)))
    const walk = (v) => {
      if (Array.isArray(v)) v.forEach(walk)
      else if (v && typeof v === 'object') {
        for (const [k, x] of Object.entries(v)) { if (extras.includes(k)) leaks.add(k); walk(x) }
      }
    }
    let keys = []
    try { const parsed = JSON.parse(body); keys = Object.keys(parsed); walk(parsed) } catch { keys = ['UNREADABLE'] }
    const line = `${req.method} ${req.url} ${keys.join(',')}${leaks.size ? ' LEAK ' + [...leaks].join(',') : ''}`
    appendFileSync('/tmp/request-fields.txt', line + '\n')
    res.writeHead(200, { 'content-type': 'text/event-stream' })
    res.end(events.map(([e, d]) => `event: ${e}\ndata: ${JSON.stringify(d)}\n\n`).join(''))
  })
}).listen(8799, '127.0.0.1')
