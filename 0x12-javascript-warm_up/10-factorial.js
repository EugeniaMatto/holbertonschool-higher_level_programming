#!/usr/bin/node
/* script */
const argv = process.argv;
const myVar = parseInt(argv[2]);
if (!myVar) {
  console.log('1');
} else {
  console.log(factorial(myVar));
}

function factorial (n) {
  if (n < 2) {
    return (1);
  }
  return (factorial(n - 1) * n);
}
