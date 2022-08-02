#!/usr/bin/node
const callMeMoby = function (n, f) {
  for (let i = 0; i < n; i++) {
    f();
  }
};
exports.callMeMoby = callMeMoby;
