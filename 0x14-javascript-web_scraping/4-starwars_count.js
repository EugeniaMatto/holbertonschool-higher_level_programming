#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];
const pj = '18';

axios.get(url)
  .then(function (response) {
    const results = response.data.results;
    let pelis = 0;
    results.forEach(r => {
      (r.characters).forEach(c => {
        if (c.includes(pj)) { pelis++; }
      });
    });
    console.log(pelis);
  });
