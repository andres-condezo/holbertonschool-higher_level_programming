#!/usr/bin/node
// a script that prints a message depending of the number of arguments passed

const arg = process.argv[2];

if (!arg) {
  console.log('No argument');
} else {
  console.log(arg);
}
