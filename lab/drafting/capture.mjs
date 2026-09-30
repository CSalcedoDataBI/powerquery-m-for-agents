// Privacy check, run before any real call: a stand-in for the DeepSeek API on 127.0.0.1
// inside the container. It records the top-level fields of each request body and answers
// 400, so dsh stops without retrying. run_dsh.ps1 points DEEPSEEK_BASE_URL here with a fake
// key and fails if a field the privacy patch should remove is still sent.
import { createServer } from 'node:http'
import { appendFileSync } from 'node:fs'

createServer((req, res) => {
  let body = ''
  req.on('data', (c) => { body += c })
  req.on('end', () => {
    let keys = []
    try { keys = Object.keys(JSON.parse(body)) } catch { keys = ['<not json>'] }
    appendFileSync('/tmp/request-fields.txt', `${req.method} ${req.url} ${keys.join(',')}\n`)
    res.writeHead(400, { 'content-type': 'application/json' })
    res.end(JSON.stringify({ type: 'error', error: { type: 'invalid_request_error', message: 'privacy check' } }))
  })
}).listen(8799, '127.0.0.1')
