#!/usr/bin/node

const argv = process.argv;
const n1 = parseInt(argv[2]);

if (isNaN(n1)) {
  console.log(1);
} else {
  let ans = 1;
  for (let i = 2; i <= n1; i++) {
    ans *= i;
  }
  console.log(ans);
}
