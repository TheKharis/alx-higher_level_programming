#!/usr/bin/node

/* A class Rectangle that defines a rectangle
 * must use the class notation for defining your class
 * the constructor must take 2 arguments w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 */

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) { // create an empty object
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
