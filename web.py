import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 8000))

HOME_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ONU Werewolf Home</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 2em; background: #f9f9f9; color: #222; }
    .container { max-width: 800px; margin: auto; background: #fff; padding: 2em; border-radius: 8px; box-shadow: 0 2px 8px #0001; }
    h1 { color: #2c3e50; }
    a { color: #2980b9; }
    .links { margin-top: 2em; }
  </style>
</head>
<body>
  <div class="container">
    <h1>ONU Werewolf</h1>
    <p>Welcome to the ONU Werewolf web portal!</p>
    <div class="links">
      <p><a href="/terms-of-service">Terms of Service</a></p>
      <p><a href="/privacy-policy">Privacy Policy</a></p>
      <p><a href="https://netgames.io/games/onu-werewolf/new" target="_blank">Start a New Game</a></p>
    </div>
    <hr>
    <p style="font-size:0.9em;color:#888;">&copy; 2025 ONU Werewolf. Not affiliated with Discord or netgames.io.</p>
  </div>
</body>
</html>
'''

class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(HOME_HTML.encode('utf-8'))
        elif self.path == "/terms-of-service":
            # Simple inline terms page
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>Terms of Service</h1><p>See the main site for details.</p>')
        elif self.path == "/privacy-policy":
            # Simple inline privacy policy page
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''<h1>Privacy Policy</h1><p>No personal data is collected or stored by this service, except as required by Discord or your hosting provider. For questions, contact the developer on Discord.</p>''')
        elif self.path == "/verify-user":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''<h1>ONU Werewolf Verification</h1><p>If you are seeing this page, the verification URL is working! You may now use this URL in your Discord server's role Links settings as a requirement for role verification.</p>''')
        elif self.path == "/api/interactions":
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 Not Found</h1>')
    def do_POST(self):
        if self.path == "/api/interactions":
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            # For demonstration, just echo back the received JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 Not Found</h1>')

if __name__ == "__main__":
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, WebHandler)
    print(f"Serving ONU Werewolf Home on port {PORT}")
    httpd.serve_forever()
