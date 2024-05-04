#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (!c) c = 'X';
    this.print(c);
  }
};
