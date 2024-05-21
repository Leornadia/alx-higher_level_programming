#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./2-statuscode.js URL');
  process.exit(1);
}

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
    return;
  }

  console.log(`code: ${response.statusCode}`);
});
