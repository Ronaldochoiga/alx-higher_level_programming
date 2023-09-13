#!/usr/bin/node
// script that concats 2 swtrings or content

const args = process.argv.slice(2);
const file = require('fs');
const contA = file.readFileSync('./' + args[0]);
const contB = file.readFileSync('./' + args[1]);
file.writeFileSync('./' + args[2], contA + contB);
