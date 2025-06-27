import os
from http.server import BaseHTTPRequestHandler, HTTPServer

REDIRECT_URL = "https://netgames.io/games/onu-werewolf/new"
PORT = int(os.environ.get("PORT", 8080))

class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(302)
        self.send_header('Location', REDIRECT_URL)
        self.end_headers()

if __name__ == "__main__":
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, RedirectHandler)
    print(f"Serving redirect on port {PORT} -> {REDIRECT_URL}")
    httpd.serve_forever()
