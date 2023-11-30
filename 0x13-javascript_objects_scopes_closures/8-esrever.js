#!/usr/bin/node

function esrever (list) {
  const n = list.length;
  const mid = n / 2;
  for (let i = 0; i < mid; i++) {
    const tmp = list[i];
    list[i] = list[n - 1 - i];
    list[n - 1 - i] = tmp;
  }
  return list;
}
module.exports = { esrever };
