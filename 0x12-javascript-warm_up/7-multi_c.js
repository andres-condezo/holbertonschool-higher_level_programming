#!/usr/bin/node
// a script that prints x times “C is fun”

const arg = parseInt(process.argv[2]);
const msg = 'C is fun';

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < arg; i++) {
  console.log(msg);
}
