#!/usr/bin/node

const value = process.argv;

if (value.length > 3) {
  console.log(value[2]);
} else {
  console.log('No argument');
}
