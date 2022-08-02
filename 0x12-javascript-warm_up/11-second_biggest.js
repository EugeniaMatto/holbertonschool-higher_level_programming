#!/usr/bin/node
/* script */
const argv = process.argv.slice(2);
argv.sort();
if (argv.length < 2) {
  console.log(0);
} else {
  console.log(argv[argv.length - 2]);
}
