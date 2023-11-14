#!/usr/bin/node

const argv = process.argv;
const n1 = parseInt(argv[2]);

function findFactorial (n) {
  if (n === 1) {
    return (1);
  }
  return n * findFactorial(n - 1);
}

if (isNaN(n1)) {
  console.log(1);
} else {
  let ans = 1;
  ans = findFactorial(n1);
  console.log(ans);
}
