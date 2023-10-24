#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const dta = JSON.parse(body);
  const dd = dta.characters;
  for (const i of dd) {
    req.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const dta1 = JSON.parse(body1);
      console.log(dta1.name);
    });
  }
});
