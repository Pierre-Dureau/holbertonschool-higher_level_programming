#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
try {
  const fileA = fs.readFileSync(args[2], 'utf8');
  const fileB = fs.readFileSync(args[3], 'utf8');
  const text = fileA + fileB;
  fs.writeFile(args[4], text, err => {
    if (err) {
      console.error(err);
    }
  });
} catch (err) {
  console.error(err);
}
