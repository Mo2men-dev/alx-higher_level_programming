#!/usr/bin/node
const { argv } = require('process');
const i = argv[2];
let msg = 'Missing number of occurrences';

if (!(Number(i))) {
  console.log(msg);
} else {
  msg = 'C is fun';
  for (let j = 0; j < i; j++) {
    console.log(msg);
  }
}
