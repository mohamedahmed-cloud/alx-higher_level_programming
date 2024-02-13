#!/usr/bin/node
const myVar = process.argv[2];
if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (process.argv[2] !== undefined && process.argv[3] === undefined) {
  console.log('Argument found');
} else if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
  console.log('Arguments found');
}
