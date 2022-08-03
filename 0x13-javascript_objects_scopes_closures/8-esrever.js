#!/usr/bin/node

exports.esrever = function (list) {
  const i = [];
  for (let j = list.length; j > 0; j--) {
    i.push(list[j - 1]);
  }
  return (i);
};
