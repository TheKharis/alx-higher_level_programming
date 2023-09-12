#!/usr/bin/node
const list = require('./data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
