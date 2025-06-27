// Open the redirect.html page in the default browser when run with Node.js
const path = require('path');
const { exec } = require('child_process');
const filePath = path.join(__dirname, 'redirect.html');

let command;
switch (process.platform) {
  case 'win32':
    command = `start "" "${filePath}"`;
    break;
  case 'darwin':
    command = `open "${filePath}"`;
    break;
  default:
    command = `xdg-open "${filePath}"`;
}
exec(command);