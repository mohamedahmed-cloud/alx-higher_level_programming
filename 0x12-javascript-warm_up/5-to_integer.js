#!/usr/bin/node

const argv = process.argv;
const cnt = argv.length;

if (cnt === 2) {
  console.log('Not a number');
} else {
  const num = parseInt(argv[2]);
  if (!isNaN(num)) {
    console.log(`My number: ${num}`);
  } else {
    console.log('Not a number');
  }
}
