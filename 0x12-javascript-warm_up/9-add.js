#!/usr/bin/node

const argv = process.argv;
const n1 = parseInt(argv[2]);
const n2 = parseInt(argv[3]);

if (isNaN(n1) || isNaN(n2)) {
  console.log('NaN');
} else {
  console.log(n1 + n2);
}
