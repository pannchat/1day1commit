let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');


let count = input[0];
const elList = input[1].split('').map(el => Number(el));
const sum = elList.reduce((acc, cur) => {return acc+cur});
console.log(sum);
