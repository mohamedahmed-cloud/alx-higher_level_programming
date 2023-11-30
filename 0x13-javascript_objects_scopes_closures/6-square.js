#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (chr = 'X') {
    super.print(chr);
  }
}
module.exports = Square;
