#!/usr/bin/node

const argv = process.argv;
const size = parseInt(argv[2]);

if (argv.length === 2 || isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let curr = '';

    for (let j = 0; j < size; j++) {
      curr += 'X';
    }
    console.log(curr);
  }
}
