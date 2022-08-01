#!/usr/bin/node
/* script that prints JavaScript is amazing */
const argv = process.argv;
let myVar;
if (!argv[2]) {
  myVar = 'No argument';
} else if (!argv[3]) {
  myVar = 'Argument found';
} else {
  myVar = 'Arguments found';
}
console.log(myVar);
