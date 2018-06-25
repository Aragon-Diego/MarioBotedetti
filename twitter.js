console.log("the bot is starting");
var Twit = require('twit');
var config = require('./config');
var T = new Twit(config);
setInterval(tw, 1000 * 20);
///tw();

function poem() {
  var fs = require("fs");
  var r = "";
  do {
    var text = fs.readFileSync("poems.txt").toString('utf-8');
    var textByLine = text.split("\n");
    var r1 = Math.floor((Math.random() * (textByLine.length - 2)) + 1);
    r = textByLine[r1];
    console.log(r1);
  } while (r.length > 280);
  console.log(r);
  return r;
}

function tw() {
  var twitt = {
    status: poem(),
  }
  T.post('statuses/update', twitt, twitted);

  function twitted(err, data, response) {
    if (err) {
      console.log("hubo un error");
    } else {
      console.log("posted");
    }
  } //maldito to
}
