#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./6-completed_tasks.js API_URL');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        completedTasks[userId] = (completedTasks[userId] || 0) + 1;
      }
    });

    console.log(completedTasks);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
