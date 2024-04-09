#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint(c = 'X') {
    if (this.width === undefined || this.height === undefined) {
      return;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
