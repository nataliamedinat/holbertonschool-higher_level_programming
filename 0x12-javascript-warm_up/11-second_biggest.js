#!/usr/bin/node

const filtr = (value, index, self) => {
  return self.indexOf(value) === index;
};

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const array = argv.slice(2);
  const ConvertArr = array.map(Number);
  const filt = ConvertArr.filter(filtr);
  const arraySort = filt.sort(function (a, b) { return a - b; });
  const FinalArr = arraySort[arraySort.length - 2];
  console.log(FinalArr);
}
