#!/usr/bin/node
const addMeMaybe = function (n, f) {
  f(n + 1);
};
exports.addMeMaybe = addMeMaybe;
