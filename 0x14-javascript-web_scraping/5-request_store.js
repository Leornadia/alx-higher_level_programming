#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length <= 3) {
  console.log('Usage: ./5-request_store.js URL FILE_PATH');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
