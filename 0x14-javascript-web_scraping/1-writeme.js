#!/usr/bin/node

const fs = require('fs');

function writeToFile(filePath, content) {
    fs.writeFile(filePath, content, 'utf8', (err) => {
        if (err) {
            console.error(`Error writing to ${filePath}: ${err}`);
        } else {
            console.log(`Content successfully written to ${filePath}`);
        }
    });
}

if (process.argv.length !== 4) {
    console.error('Usage: node script.js <file_path> <content>');
} else {
    const filePath = process.argv[2];
    const content = process.argv[3];
    writeToFile(filePath, content);
}

