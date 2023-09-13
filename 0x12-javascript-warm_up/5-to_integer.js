#!/usr/bin/node

// Script that prints integers as added as arguments

const myArg = process.argv[2];

if (isNaN(Number(myArg))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myArg);
}
