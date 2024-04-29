#!/usr/bin/node

const { argv } = require('process');

if (argv.length === 3) {
  console.log('Argument found');
}

else if (argv.lenght > 3) {
  console.log('Arguments found');
}

else {
  console.log('No argument');
}
