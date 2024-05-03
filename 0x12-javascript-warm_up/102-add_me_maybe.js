#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  Number(number) ? theFunction(Number(number) + 1) : theFunction(Number(number))
}
