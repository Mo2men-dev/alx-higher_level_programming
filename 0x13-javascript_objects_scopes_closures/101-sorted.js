#!/usr/bin/node
const { dict } = require('./101-data.js');
const outDict = {};
for (const i in dict) {
  outDict[dict[i]] ? outDict[dict[i]].push(i) : outDict[dict[i]] = [i];
}
console.log(outDict);
