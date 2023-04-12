#!/usr/bin/node

/* A function that executes x times a function
 * The function must be visible from outside
 */

exports.callMeMoby = function callMeMoby (x, theFunction) { // function takes 2 parameters, x and theFunction
  if (x > 0) {
    theFunction(); // function to be executed
    callMeMoby(x - 1, theFunction);
  }
};
