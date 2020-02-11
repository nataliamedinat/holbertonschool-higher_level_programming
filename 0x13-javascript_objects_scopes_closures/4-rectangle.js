#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let trav = 0; trav < this.height; trav++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const rheight = this.height;
    const rwidth = this.width;
    this.width = rheight;
    this.height = rwidth;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
