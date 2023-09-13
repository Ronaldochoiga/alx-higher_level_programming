#!/usr/bin/node

// script prints a reversed version of a list

exports.esrever = function (list) {
  const nwList = [];
  const lInd = list.length - 1;
  for (let i = lInd, j = 0; i >= 0; i--, j++) {
    nwList[j] = list[i];
  }
  return nwList;
};
