#!/usr/bin/node
const args = process.argv;
let str;
if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(args[2]); i++) {
    str = '';
    for (let j = 0; j < parseInt(args[2]); j++) {
      str += 'X';
    }
    console.log(str);
  }
}
