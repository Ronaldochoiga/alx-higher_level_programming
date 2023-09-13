#!/usr/bin/node

// script converts num to a given base

exports.converter = function (base) {
  function nwBase (num) {
      return num.toString(base);
  }

  return nwBase;
};
