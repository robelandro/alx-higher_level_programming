#!/usr/bin/node

const value = process.argv;

if (value.length === 3) {
  console.log('Argument found');
} else if (value.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
