#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;

axios.get(args[2])
  .then(function (response) {
    let n = 0;
    response.data.results.forEach(str => {
      if (str.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        n++;
      }
    });
    console.log(n);
  });
