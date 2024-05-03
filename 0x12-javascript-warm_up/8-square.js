#!/usr/bin/node
const { argv, stdout } = require('process');
const i = argv[2];
let msg = 'Missing size';

if (!(Number(i))) {
  console.log(msg);
} else {
  msg = 'X';
  for (let x = 0; x < i; x++) {
    for (let y = 0; y < i; y++) {
      stdout.write(msg);
    }
    console.log();
  }
}
