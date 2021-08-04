#!/usr/bin/node
// a class Square that defines a square and inherits from Square
//
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
