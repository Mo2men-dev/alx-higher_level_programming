#!/usr/bin/node
const { argv } = require('process');

function add (a, b) {
  const result = Number(a) + Number(b);
  return Number(result);
}

console.log(add(argv[2], argv[3]));
