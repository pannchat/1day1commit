let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = parseInt(input.shift());
input.sort();
input.sort((x,y)=>{
    return x.length-y.length
})


let res = [...new Set(input)];
res.map((el) => {
    console.log(el)
})