#!/usr/bin/node

// script that prints rectangle using character x

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rows = 'X';
    for (let i = 0; i < this.width - 1; i++) {
      rows += 'X';
    }
    for (let b = 0; b < this.height; b++) {
      console.log(rows);
    }
  }
};
