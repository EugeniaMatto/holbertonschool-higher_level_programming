#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];
const file = require('fs');
const nameFile = process.argv[2];

axios.get(url)
  .then(function (response) {
    file.appendFile(nameFile, data, { encoding: 'utf8' },
      function (error) {
        if (error) { console.log(error); }
      });
  });
