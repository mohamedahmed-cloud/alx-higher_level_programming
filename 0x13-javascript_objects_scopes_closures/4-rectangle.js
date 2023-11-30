#!/usr/bin/node

class Rectangle {
  constructor (w = 0, h = 0) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (chr="X") {
    let curr = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        curr += chr;
      }
      curr += '\n';
    }
    console.log(curr.slice(0, -1));
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
