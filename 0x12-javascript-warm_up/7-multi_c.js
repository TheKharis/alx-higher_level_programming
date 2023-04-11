#!/usr/bin/node

/* A script that prints x times “C is fun”
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer, print “Missing number of occurrences”
 */

const arg = process.argv[2];

if (isNaN(parseInt(arg))) {
  console.log('Missing Number of occurrences');
} else {
  const x = parseInt(arg);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
