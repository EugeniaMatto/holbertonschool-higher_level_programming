#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];

axios.get(url)
  .then(function (response) {
    console.log('code: 200');
  })
  .catch(error => {
    console.log('code: 404');
  });
