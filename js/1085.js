let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
const [x,y,w,h] = input;
let res = [];

res.push(x)
res.push(y)
res.push(Math.abs(x-w))
res.push(Math.abs(y-h))
console.log(Math.min(...res))