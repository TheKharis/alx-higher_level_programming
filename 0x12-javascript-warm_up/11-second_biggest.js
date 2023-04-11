#!/usr/bin/node

/* A script that searches the second biggest integer in the list of arguments
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 */

const args = process.argv.slice(2).map(arg => parseInt(arg));

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const sortedArguments = args.sort((a, b) => b - a);
  console.log(sortedArguments[1]);
}
