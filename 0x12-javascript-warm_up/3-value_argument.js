#!/usr/bin/node

/* A script that prints the first argument passed to it
 * If no arguments are passed to the script, print “No argument”
 */

const arg = process.argv[2];

if (arg === undefined) { // No argument passed
  console.log('No argument');
} else {
  console.log(arg);
}
