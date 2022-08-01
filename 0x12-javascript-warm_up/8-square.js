#!/usr/bin/node
/* script */
const argv = process.argv;
const n = parseInt(argv[2]);
if (!n) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    console.log('X'.repeat(n));
  }
}
