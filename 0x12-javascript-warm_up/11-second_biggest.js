#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const newArgv = argv.slice(2).map(val => parseInt(val));
  const mx = Math.max(...newArgv);
  let ans = Number.MIN_SAFE_INTEGER;

  for (let i = 2; i < argv.length; i++) {
    if (parseInt(argv[i]) !== mx) {
      ans = Math.max(argv[i], ans);
    }
  }
  console.log(ans);
}
