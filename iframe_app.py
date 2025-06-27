import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 8080))

IFRAME_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ONU Werewolf IFrame App</title>
  <style>body,html{margin:0;padding:0;height:100%;}</style>
</head>
<body style="height:100%;margin:0;">
  <iframe src="https://netgames.io/games/onu-werewolf/new" style="border:none;width:100vw;height:100vh;"></iframe>
</body>
</html>
'''

class IFrameHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(IFRAME_HTML.encode('utf-8'))

if __name__ == "__main__":
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, IFrameHandler)
    print(f"Serving ONU Werewolf IFrame app on port {PORT}")
    httpd.serve_forever()
