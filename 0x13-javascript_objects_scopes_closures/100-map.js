#!/usr/bin/node
const { list } = require('./100-data.js');
const outList = list.map((x, i) => x * i);
console.log(list);
console.log(outList);
