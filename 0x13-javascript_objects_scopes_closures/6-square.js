#!/usr/bin/node

const mainSquare = require('./5-square');

class Square extends mainSquare {
  charPrint (chr = 'X') {
    super.print(chr);
  }
}
module.exports = Square;
