#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tsks = JSON.parse(body);
    for (const i in tsks) {
      const tsk = tsks[i];
      if (tsk.completed === true) {
        if (completed[tsk.userId] === undefined) {
          completed[tsk.userId] = 1;
        } else {
          completed[tsk.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
