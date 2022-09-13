#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];
dict = {
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
  10: 0
};

axios.get(url)
  .then(function (response) {
    const all = response.data;
    all.forEach(function (e) {
      if (e.completed) {
        let ch = String.fromCharCode(48 + e.userId);
        if (ch == ':') { ch = '10'; }
        dict[ch] = dict[ch] + 1;
      }
    });
    for (const [k, v] of Object.entries(dict)) {
      if (v == 0) { delete dict.k; }
    }
    console.log(dict);
  });
