#!/usr/bin/node
/* script that prints JavaScript is amazing */
const argv = process.argv;
let myVar;
if (!argv[2]) {
  myVar = 'No argument';
} else {
  myVar = argv[2];
}
console.log(myVar);
