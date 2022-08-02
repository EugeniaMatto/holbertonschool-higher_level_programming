#!/usr/bin/node
/* script */
const argv = process.argv;
if (!argv[2] || !argv[3]) {
  console.log(0);
} else {
  argv.shift();
  argv.shift();
  argv.sort();
  console.log(argv[argv.length - 2]);
}
