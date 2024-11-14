#!/usr/bin/env node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a Movie ID as an argument');
  process.exit(1);
}

// URL to get the movie details based on the Movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie data');
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Function to get each character's name and print it in order
  const getCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) reject(error);
        else resolve(JSON.parse(body).name);
      });
    });
  };

  // Fetch character names in the same order as the list
  Promise.all(characterUrls.map(getCharacterName))
    .then((characterNames) => {
      characterNames.forEach((name) => console.log(name));
    })
    .catch((error) => console.error('Error fetching character names:', error));
});

