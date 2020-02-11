#!/usr/bin/node
exports.esrever = function (list) {
  const new_ = [];
  for (let trav = list.length - 1; trav >= 0; trav--) {
    new_.push(list[trav]);
  }
  return new_;
};
