var fs = require("fs");
var r = "";
do {
  var text = fs.readFileSync("poems.txt").toString('utf-8');
  var textByLine = text.split("\n");
  r = textByLine[Math.floor((Math.random() * (textByLine.length - 2)) + 1)];
} while (r.length > 10);
console.log(r);
