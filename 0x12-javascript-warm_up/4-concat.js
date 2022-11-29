#!/usr/bin/node

const value = process.argv;

if (value[3]) {
  console.log(value[2] + ' is ' + value[3]);
}
