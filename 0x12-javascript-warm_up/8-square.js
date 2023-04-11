#!/usr/bin/node

/* A script that prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 */

const arg = process.argv[2];

if (isNaN(parseInt(arg))) {
  console.log('Missing size');
} else {
  const size = parseInt(arg);
  for (let i = 0; i < size; i++) {
    let statement = '';
    for (let k = 0; k < size; k++) {
      statement += 'X';
    }
    console.log(statement);
  }
}
