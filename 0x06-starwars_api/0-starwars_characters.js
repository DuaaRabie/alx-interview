#!/usr/bin/env node

// Import the request module
const request = require('request')

// Get the movie ID from command line arguments
const movieId = process.argv[2]

// Check if a movie ID was provided
if (!movieId) {
  console.error('Please provide a Movie ID as the first argument')
  process.exit(1)
}

// Define the URL for the Star Wars API with the given movie ID
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`

// Make a GET request to the Star Wars API for the specified movie
request(url, (err, res, body) => {
  if (err) {
    console.error('Error:', err)
    return
  }

  // Parse the response body as JSON
  const movieData = JSON.parse(body)

  // Loop through each character URL in the "characters" list
  movieData.characters.forEach(characterUrl => {
    // Make a GET request for each character
    request(characterUrl, (err, res, body) => {
      if (err) {
        console.error('Error:', err)
        return
      }

      // Parse the character data and log the character's name
      const characterData = JSON.parse(body)
      console.log(characterData.name)
    })
  })
})
