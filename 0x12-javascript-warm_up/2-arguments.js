#!/usr/bin/node
console.log('No argument');
console.log('Argument found');
console.log('Arguments found');
const { argv } = require('node:process');
console.log(argv);