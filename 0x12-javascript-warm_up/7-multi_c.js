#!/usr/bin/node
/* script */
const argv = process.argv;
const myVar = 'C is fun';
const n = parseInt(argv[2]);
if (!n) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log(myVar);
  }
}
