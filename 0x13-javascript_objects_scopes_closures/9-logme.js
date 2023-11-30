#!/usr/bin/node

let cnt = 0;
function logMe (item) {
  console.log(`${cnt}: ${item}`);
  cnt++;
}
module.exports = { logMe };
