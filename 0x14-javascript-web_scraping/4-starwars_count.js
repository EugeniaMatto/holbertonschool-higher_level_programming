#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];
const pj = 'https://swapi-api.hbtn.io/api/people/18/';

axios.get(url)
  .then(function (response) {
    const results = response.data.results;
    let pelis = 0;
    results.forEach(r => {
      if (r.characters.includes(pj)) { pelis++; }
    });
    console.log(pelis);
  });
