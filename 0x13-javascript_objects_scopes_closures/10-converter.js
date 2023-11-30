#!/usr/bin/node

function converter (base) {
  function newBase (number) {
    return number.toString(base);
  }
  return newBase;
}
module.exports = { converter };
