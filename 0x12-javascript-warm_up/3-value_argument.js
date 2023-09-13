#!/usr/bin/node

// Script that traces presence of arguments

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
