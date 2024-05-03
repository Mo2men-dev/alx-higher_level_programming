#!/usr/bin/node
const { argv } = require('process');

function bubbleSort (arr) {
  let flag = 0;

  for (let i = 0; i < arr.length; i++) {
    flag = 0;

    for (let j = 0; j < arr.length - 1; j++) {
      if (Number(arr[j]) > Number(arr[j + 1])) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        flag = 1;
      }
    }

    if (flag === 0) return arr;
  }
}

if (argv.length <= 3) {
  console.log(Number(0));
} else {
  const arr = bubbleSort(argv.slice(2));
  console.log(Number(arr[arr.length - 2]));
}
