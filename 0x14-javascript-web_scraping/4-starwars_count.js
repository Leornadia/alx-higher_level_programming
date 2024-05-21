#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./4-starwars_count.js API_URL');
  process.exit(1);
}

const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode === 200) {
    const moviesData = JSON.parse(body).results;
    const moviesWithWedge = moviesData.filter((movie) =>
      movie.characters.some((characterUrl) =>
        characterUrl.includes(`/api/people/${wedgeAntillesId}/`)
      )
    );
    console.log(moviesWithWedge.length);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
