#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorialize (a) {
  if (a === 0 || a === 1) {
    return 1;
  }
  return factorialize(a - 1) * a;
}
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorialize(num));
}
