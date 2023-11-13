#!/usr/bin/node
const argv = process.argv;
const length = argv.length;
if (length === 2) {
  console.log('No argument');
} else if (length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
