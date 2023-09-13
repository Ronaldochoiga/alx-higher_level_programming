#!/usr/bin/node
// executes a function x times

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
