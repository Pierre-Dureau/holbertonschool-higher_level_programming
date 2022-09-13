#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];

axios.get(url).then(function (response) {
  console.log(response.data.title);
});
