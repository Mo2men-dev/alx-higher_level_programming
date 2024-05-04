#!/usr/bin/node
let logged = 0;
exports.logMe = function (item) {
  console.log(`${logged++}: ${item}`);
};
