#!/usr/bin/node
// a script that prints a square

const arg = parseInt(process.argv[2]);
const character = 'X';

if (isNaN(arg)) {
  console.log('Missing size');
}

for (let i = 0; i < arg; i++) {
  console.log(character.repeat(arg));
}
