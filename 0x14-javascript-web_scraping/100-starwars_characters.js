#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./100-starwars_characters.js movieId');
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

    const getAllCharacters = (urls) => {
      const promises = urls.map((url) => {
        return new Promise((resolve, reject) => {
          request(url, (error, response, body) => {
            if (error) {
              reject(error);
            } else if (response.statusCode === 200) {
              const characterData = JSON.parse(body);
              resolve(characterData.name);
            } else {
              reject(`Error: ${response.statusCode}`);
            }
          });
        });
      });

      return Promise.all(promises);
    };

    getAllCharacters(charactersUrls)
      .then((characterNames) => {
        characterNames.forEach((name) => {
          console.log(name);
        });
      })
      .catch((error) => {
        console.log(error);
      });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
