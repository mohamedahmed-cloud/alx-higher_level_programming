#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let cnt = 0;

  list.forEach(element => {
    if (searchElement === element) {
      cnt += 1;
    }
  });
  return cnt;
}

module.exports = { nbOccurences };
