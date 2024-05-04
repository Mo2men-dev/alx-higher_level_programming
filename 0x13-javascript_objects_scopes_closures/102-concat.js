#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');

// Function to read a file and return a promise
function readFilePromise (filename) {
  return new Promise((resolve, reject) => {
    fs.readFile(filename, (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}

// Read both files asynchronously and concatenate their contents
Promise.all([
  readFilePromise(argv[2]),
  readFilePromise(argv[3])
]).then(values => {
  const combinedContent = values.join('');

  // Write the combined content to the output file
  fs.writeFile(argv[4], combinedContent, (err) => {
    if (err) {
      throw err;
    }
  });
}).catch(err => {
  console.error('Error reading files:', err);
});
