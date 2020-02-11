#!/usr/bin/node

const Rectangle = require('./5-square');

module.exports = class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let trav = 0; trav < this.width; trav++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
