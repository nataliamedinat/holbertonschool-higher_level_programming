#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let trav = 0; trav < size; trav++) {
    console.log('X'.repeat(size));
  }
}
