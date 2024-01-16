#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;
    const wedgeAntillesMovies = filmsData.filter(movie =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );

    console.log(`${wedgeAntillesMovies.length}`);
  }
});
