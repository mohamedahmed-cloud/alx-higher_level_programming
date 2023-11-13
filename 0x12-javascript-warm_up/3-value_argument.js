#!/usr/bin/node

const argv = process.argv;
let cnt = 0;

argv.forEach(element => {
  cnt++;
});

if (cnt === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
