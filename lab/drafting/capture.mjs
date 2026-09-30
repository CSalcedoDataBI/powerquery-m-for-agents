// Privacy check, run before any real call: a stand-in for the DeepSeek API on 127.0.0.1
// inside the container. For each request it records the top-level fields, and LEAK with the
// name of either extra found anywhere in the raw body (nested or not), then answers 400 so dsh
// stops without retrying. run_dsh.ps1 points DEEPSEEK_BASE_URL here with a fake key and fails
// on any LEAK.
import { createServer } from 'node:http'
import { appendFileSync } from 'node:fs'

createServer((req, res) => {
  let body = ''
  req.on('data', (c) => { body += c })
  req.on('end', () => {
    let keys = []
    try { keys = Object.keys(JSON.parse(body)) } catch { keys = ['<not json>'] }
    const leaks = ['dsh_session_log', 'dsh_plugin_packages'].filter((f) => body.includes(f))
    const line = `${req.method} ${req.url} ${keys.join(',')}${leaks.length ? ' LEAK ' + leaks.join(',') : ''}`
    appendFileSync('/tmp/request-fields.txt', line + '\n')
    res.writeHead(400, { 'content-type': 'application/json' })
    res.end(JSON.stringify({ type: 'error', error: { type: 'invalid_request_error', message: 'privacy check' } }))
  })
}).listen(8799, '127.0.0.1')
