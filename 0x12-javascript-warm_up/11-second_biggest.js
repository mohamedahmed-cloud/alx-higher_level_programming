#!/usr/bin/node

const argv = process.argv;
const n1 = parseInt(argv[2]);

if (argv.length <= 3) {
  console.log(0);
} else {
  let mx = Math.max(...argv);
  let ans = Number.MIN_SAFE_INTEGER;

  for (let i = 2; i < argv.length; i++) {
	  if (argv[i] !== mx) {
		console.log(argv[i], "youse");
      ans = Math.max(argv[i], ans);
    }
  }
  console.log(ans);
}
