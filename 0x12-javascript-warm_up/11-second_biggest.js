#!/usr/bin/node
const args = process.argv;
let max;
let secondmax;

if (isNaN(args[3])) {
  console.log('0');
} else {
  if (parseInt(args[2]) > parseInt(args[3])) {
    max = parseInt(args[2]);
    secondmax = parseInt(args[3]);
  } else {
    max = parseInt(args[3]);
    secondmax = parseInt(args[2]);
  }
  for (let i = 4; i < args.length; i++) {
    if (parseInt(args[i]) > max) {
      secondmax = max;
      max = parseInt(args[i]);
    } else if (parseInt(args[i]) > secondmax) {
      secondmax = parseInt(args[i]);
    }
  }

  console.log(secondmax);
}
