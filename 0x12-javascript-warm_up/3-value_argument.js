#!/usr/bin/node

const value = process.argv;

if (value[2]) {
  console.log(value[2]);
} else {
  console.log('No argument');
}
