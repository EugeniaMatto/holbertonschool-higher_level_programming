#!/usr/bin/node

const request = require('fs');
const url = process.argv[2];
const data = process.argv[3];

request.appendFile(url, data, { encoding: 'utf8' }, function (error) {
  if (error) {
    console.log(error);
  }
});
