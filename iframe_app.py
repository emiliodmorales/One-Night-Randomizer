import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 8080))

IFRAME_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ONU Werewolf Discord Activity</title>
  <style>body,html{margin:0;padding:0;height:100%;}</style>
  <script src="https://discord.com/assets/2e1e6c2e3c6e2c2b2b2b.js"></script> <!-- Discord Embedded App SDK -->
  <script>
    let userName = '';
    let userAvatar = '';
    let channelName = '';
    function showLobby() {
      document.getElementById('setup').style.display = 'none';
      document.getElementById('gameframe').style.display = 'block';
      document.getElementById('lobby-display-name').textContent = userName;
      document.getElementById('lobby-avatar').src = userAvatar;
      document.getElementById('lobby-channel').textContent = channelName;
    }
    window.addEventListener('DOMContentLoaded', function() {
      if (window.DiscordNative && window.DiscordNative.user) {
        // Discord Desktop (old SDK)
        userName = window.DiscordNative.user.getCurrentUser().username;
        userAvatar = window.DiscordNative.user.getCurrentUser().avatar;
        channelName = 'Discord Channel';
        document.getElementById('user-info').innerHTML = `<img src="${userAvatar}" style="width:48px;height:48px;border-radius:50%;vertical-align:middle;"> <b>${userName}</b>`;
      } else if (window.Discord && window.Discord.client) {
        // Discord Embedded App SDK
        window.Discord.client.getCurrentUser().then(user => {
          userName = user.username;
          userAvatar = user.avatar;
          document.getElementById('user-info').innerHTML = `<img src="${userAvatar}" style="width:48px;height:48px;border-radius:50%;vertical-align:middle;"> <b>${userName}</b>`;
        });
        window.Discord.client.getChannelId().then(cid => {
          channelName = `Channel: ${cid}`;
          document.getElementById('channel-info').textContent = channelName;
        });
      } else {
        document.getElementById('user-info').textContent = 'Not running in Discord Activity.';
      }
    });
  </script>
</head>
<body style="height:100%;margin:0;">
  <div id="setup" style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100vh;">
    <h2>ONU Werewolf Discord Activity</h2>
    <div id="user-info" style="margin-bottom:1em;"></div>
    <div id="channel-info" style="margin-bottom:1em;"></div>
    <button onclick="showLobby()" style="font-size:1.2em;padding:0.5em 1em;">Start Game</button>
  </div>
  <div id="gameframe" style="display:none;height:100%;width:100vw;">
    <div id="lobby-message" style="text-align:center;margin-top:2em;font-size:1.5em;">
      Lobby started for <img id="lobby-avatar" style="width:48px;height:48px;border-radius:50%;vertical-align:middle;"> <span id="lobby-display-name"></span>!<br>
      <span id="lobby-channel"></span><br>
      (Share this lobby in Discord or continue in the app.)
    </div>
  </div>
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
