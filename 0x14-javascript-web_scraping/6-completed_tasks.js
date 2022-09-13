#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];

axios.get(url)
  .then(function (response) {
    const all = response.data;
    const dict = {};
    all.forEach(function (e) {
      if (e.completed) {
        let ch = String.fromCharCode(48 + e.userId);
        if (ch === ':') { ch = '10'; }
        if (!(Object.keys(dict).includes(ch))) { dict[ch] = 0; }
        dict[ch] = dict[ch] + 1;
      }
    });
    console.log(dict);
  });
