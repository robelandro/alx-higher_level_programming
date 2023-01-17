#!/usr/bin/node
// a script that reads and prints the content of a file.
const fs = require('fs');
const file = process.argv;

if (file[2]) {
  fs.readFile(file[2], 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
