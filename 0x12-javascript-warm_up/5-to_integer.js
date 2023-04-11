#!/usr/bin/node

/* A script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
 * if the argument can’t be converted to an integer, print “Not a number”
 */

const [arg] = process.argv.slice(2);

const numb = parseInt(arg);

if (Number.isNaN(numb)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numb}`);
}
