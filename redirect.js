// Open the ONU Werewolf game in the default browser when run with Node.js
const url = "https://netgames.io/games/onu-werewolf/new";
const { exec } = require("child_process");

let command;
switch (process.platform) {
  case "win32":
    command = `start "" "${url}"`;
    break;
  case "darwin":
    command = `open "${url}"`;
    break;
  default:
    command = `xdg-open "${url}"`;
}
exec(command);