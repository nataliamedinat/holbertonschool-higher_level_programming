#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
  for (let trav = 0; trav < this.Rectangle; trav ++) {
    console.log('X'.repeat(this.Rectangle));
}
}
};
