#!/usr/bin/node

const numberOfTimes = parseInt(process.argv[2]);

if (isNaN(numberOfTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let trav = 0; trav < numberOfTimes; trav++) {
    console.log('C is fun');
  }
}
