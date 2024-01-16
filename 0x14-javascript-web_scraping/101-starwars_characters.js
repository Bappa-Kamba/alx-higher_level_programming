#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as the first argument');
  process.exit(1);
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(`Error fetching movie data: ${error}`);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    process.exit(1);
  }

  try {
    const movieData = JSON.parse(body);
    const characterPromises = movieData.characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(`Error fetching character data: ${error}`);
          } else if (response.statusCode !== 200) {
            reject(`Failed to fetch character data. Status code: ${response.statusCode}`);
          } else {
            const character = JSON.parse(body);
            resolve(character.name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error(error);
        process.exit(1);
      });
  } catch (parseError) {
    console.error(`Error parsing movie data: ${parseError}`);
    process.exit(1);
  }
});
