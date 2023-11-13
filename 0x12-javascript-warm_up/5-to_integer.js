#!/usr/bin/node

const argv = process.argv;
const cnt = argv.length;

if (cnt == 2) {
  console.log("Not a number");
} else {
  console.log(parseInt(argv[3]));
}
