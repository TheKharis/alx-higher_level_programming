#!/usr/bin/node

/* A script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 */

function factorial (x) {
  if (isNaN(parseInt(x))) {
    return 1;
  } else if (x <= 1) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}

const arg = process.argv[2];
const x = parseInt(arg);
console.log(factorial(x));
