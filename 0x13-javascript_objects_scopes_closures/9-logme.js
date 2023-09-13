#!/usr/bin/node

// script prints no of arg and the nw value

function * generator () {
  let indx = 0;
  while (true) {
    yield indx++;
  }
}

const gen = generator();

exports.logMe = function (itm) {
  console.log(gen.next().value + ': ' + itm);
};
