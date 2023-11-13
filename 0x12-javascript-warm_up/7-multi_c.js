#!/usr/bin/node

const argv = process.argv;
const cnt = argv[2];

if (argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < cnt; i++) {
    console.log('C is fun');
  }
}
