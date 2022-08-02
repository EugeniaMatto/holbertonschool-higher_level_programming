#!/usr/bin/node
/* script */
const argv = process.argv;
const myVar = [];
if (!argv[2]) {
  console.log(0);
} else if (!argv[3]) {
  console.log(argv[2]);
} else {
  let i = 0;

  for (const elem of argv) {
    i++;
    if (i > 2) {
      myVar.push(parseInt(elem));
    }
  }
  myVar.sort();
  console.log(myVar[myVar.length - 2]);
}
