#!/usr/bin/node
// function shows no of occurencies in a list

const orgList = require('./100-data').list;
console.log(orgList);
const mpdList = orgList.map (function (e, indx) {
    return (e * indx);
});
console.log(mpdList);
