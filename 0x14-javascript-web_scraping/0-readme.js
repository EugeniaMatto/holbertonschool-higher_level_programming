#!/usr/bin/node

const request = require('fs');
const url = process.argv[2];

request.readFile(url, { encoding: 'utf8' }, function (error, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(body.toString());
  }
});
