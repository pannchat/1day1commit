let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

input.forEach( el => {
    if(el === '0') return
    console.log(el === el.split('').reverse().join('')? 'yes' : 'no');
})