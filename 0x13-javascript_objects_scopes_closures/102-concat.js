#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
const file1 = argv[2];
const file2 = argv[3];
const file3 = argv[4];

fs.readFile(file1, 'utf-8', (err, file1) => {
  if (err) throw err;

  fs.readFile(file2, 'utf-8', (err, file2) => {
    if (err) throw err;

    const finalContent = file1 + '\n' + file2;
    fs.writeFile(file3, finalContent, (err, file) => {
      if (err) throw err;
    });
  });
});
