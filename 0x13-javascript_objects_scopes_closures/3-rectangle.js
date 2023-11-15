#!/usr/bin/node

class Rectangle {
  constructor (w = 0, h = 0) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let curr = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        curr += 'X';
      }
      curr += '\n';
    }
    console.log(curr.slice(0, -1));
  }
}
module.exports = Rectangle;
