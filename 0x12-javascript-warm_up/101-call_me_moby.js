#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let trav = 0; trav < x; trav++) {
    theFunction();
  }
};
