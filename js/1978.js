let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = parseInt(input.shift());

const arr = input.shift().split(' ').map(e=>+e);
const prime = new Array(1001).fill(true);
let count = 0;
prime[0] = false;
prime[1] = false;
for(let i = 2; i<=1000; i++){
    for(let j=i+i; j<=1000; j+=i){
        prime[j]=false;
    }
}
arr.forEach(num => {
    if(prime[num]) count++;
})

console.log(count);