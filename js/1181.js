let fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = input.shift();
const sorted = input.sort((a, b) => a.length - b.length || a.localeCompare(b));
const uniqueValues = new Set(sorted);
console.log(Array.from(uniqueValues).join('\n'));