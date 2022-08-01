#!/usr/bin/node
/* script */
const argv = process.argv;
let myVar = parseInt(argv[2]);
if (!myVar) {
  myVar = 'Not a number';
} else {
  myVar = 'My number: ' + myVar;
}
console.log(myVar);
