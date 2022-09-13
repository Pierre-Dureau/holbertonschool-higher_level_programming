#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];

async function doGetRequest() {
  const response = await axios.get(url)
  for (let i = 0; i < response.data.characters.length; i++) {
    const name = await axios.get(response.data.characters[i]);
    console.log(name.data.name);
  }
}
doGetRequest();
