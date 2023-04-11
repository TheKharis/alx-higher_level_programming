#!/usr/bin/node

/* A script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 */

function add (a, b) { // function to add two integers
  return (a + b);
}

const arg1 = process.argv[2]; // read first argument
const arg2 = process.argv[3]; // read second argument

const a = parseInt(arg1);
const b = parseInt(arg2);

const sum = add(a, b);

console.log(sum);
