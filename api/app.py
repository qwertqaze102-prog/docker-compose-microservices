#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import redis

r = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://localhost:6379/0"))


class Handler(BaseHTTPRequestHandler):
    def _json(self, code, payload):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/api/health":
            try:
                r.ping()
                self._json(200, {"status": "ok", "redis": "up"})
            except Exception as e:
                self._json(503, {"status": "degraded", "error": str(e)})
        elif self.path == "/api/jobs":
            n = r.llen("jobs")
            self._json(200, {"queue_length": n})
        else:
            self._json(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/jobs":
            self._json(404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            data = json.loads(raw.decode() or "{}")
        except json.JSONDecodeError:
            self._json(400, {"error": "invalid json"})
            return
        task = data.get("task", "noop")
        r.rpush("jobs", json.dumps({"task": task}))
        self._json(202, {"accepted": True, "task": task})

    def log_message(self, fmt, *args):
        return


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
