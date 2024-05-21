#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./101-starwars_characters.js movieId');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    if (charactersUrls.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    const getCharacterName = (url, callback) => {
      request(url, (error, response, body) => {
        if (error) {
          callback(null, null);
          return;
        }

        if (response.statusCode === 200) {
          const characterData = JSON.parse(body);
          callback(null, characterData.name);
        } else {
          callback(null, null);
        }
      });
    };

    charactersUrls.forEach((url) => {
      getCharacterName(url, (error, name) => {
        if (name !== null) {
          console.log(name);
        }
      });
    });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
