let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = parseInt(input.shift())
let num=666
let cnt = 1;
while(cnt !== n){
 num++;
    if(String(num).includes('666')) cnt++;
}
console.log(num);