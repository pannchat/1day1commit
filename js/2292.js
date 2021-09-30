let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = parseInt(input.shift());

let cnt = 1;
let range = 1;
while(true){
    if(range >= n){
        break;
    }
    let tmp = cnt++ * 6;
    range += tmp;

}
console.log(cnt)