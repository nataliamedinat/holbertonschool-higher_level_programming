#!/usr/bin/node

const filtr = (value, index, self) => {
  return self.indexOf(value) === index;
};

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const array = argv.slice(2);
  const m_array = array.map(Number);
  const filt = m_array.filter(filtr);
  const array_sort = filt.sort(function (a, b) { return a - b; });
  const final_arr = array_sort[array_sort.length - 2];
  console.log(final_arr);
}
