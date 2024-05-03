#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  if (!Number(x)) {
    theFunction();
  } else {
    for (let i = 0; i < Number(x); i++) {
      theFunction();
    }
  }
};
