#!/usr/bin/node

// Script that prints square of size arg[2]

const myArg = process.argv[2];
let rows = 'X';

if (isNaN(Number(myArg))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myArg - 1; i++) {
    rows += 'X';
  }
  for (let b = 0; b < myArg; b++) {
    console.log(rows);
  }
}
