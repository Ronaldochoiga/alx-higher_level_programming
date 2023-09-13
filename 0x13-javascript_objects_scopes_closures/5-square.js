#!/usr/bin/node
// this script uses super() to call class and uses extend
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
