#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;

axios.get(args[2]).then(function (response) {
  let n = 0;
  response.data.results.forEach(film => {
    film.characters.forEach(char => {
      if (char.includes('18')) {
        n++;
      }
    });
  });
  console.log(n);
});
