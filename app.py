import http.server
import os

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Dockerfile-built PHP-look-alike repository on NjiraCloud")

port = int(os.environ.get("PORT", "8080"))
http.server.HTTPServer(("0.0.0.0", port), Handler).serve_forever()
