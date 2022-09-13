#!/usr/bin/node
const args = process.argv;
const axios = require('axios').default;

axios.get(args[2]).then(function (response) {
  const alltasks = {};
  response.data.forEach(task => {
    const id = task.userId;
    let nb = alltasks[id];
    if (!nb) {
      nb = 0;
    }
    if (task.completed) {
      alltasks[id] = nb + 1;
    }
  });
  console.log(alltasks);
});
