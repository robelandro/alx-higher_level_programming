#!/usr/bin/node
// a script that writes a string to a file.

const fs = require('fs');
const file = process.argv;

if (file[2] && file[3]) {
  fs.writeFile(file[2], file[3], 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
}
