#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ocurr = 0;

  for (let trav = 0; trav < list.length; trav++) {
    if (list[trav] === searchElement) {
      ocurr++;
    }
  }
  return ocurr;
};
