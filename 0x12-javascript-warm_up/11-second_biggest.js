#!/usr/bin/node
/* script */
const argv = process.argv.slice(2);
argv.sort();
argv.reverse();
if (argv.length < 2) {
  console.log(0);
} else {
  while (argv[0] === argv[1]) {
    argv.shift();
  }
  if (!argv[1]) {
    console.log(0);
  } else {
    console.log(argv[1]);
  }
}
