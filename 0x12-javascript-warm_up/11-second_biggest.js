#!/usr/bin/node

const argv = process.argv;
const n1 = parseInt(argv[2]);

if (isNaN(n1)) {
  console.log(0);
} else {
  const newArgv = argv.slice(2).map(val => parseInt(val));
  const mx = Math.max(...newArgv);
  let ans = Number.MIN_SAFE_INTEGER;

  for (let i = 2; i < argv.length - 1; i++) {
    if (argv[i] !== mx) {
      ans = Math.max(argv[i], ans);
    }
  }
  console.log(ans);
}
