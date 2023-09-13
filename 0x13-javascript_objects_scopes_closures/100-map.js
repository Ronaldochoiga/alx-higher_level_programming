#!/usr/bin/node
// script that imports arrays

const orgList = require('./100-data').list;
console.log(orgList);
const mpdList = orgList.map (function (e, index) {
    return (e * index);
});
console.log(mpdList);
