let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const isPrime = (num) => {
    if(num === 1) return false;
    for(var i=2; i<=Math.sqrt(num); i++){
        if((num%i)==0) return false;
    }
    return true;
}

const [n,m] = input.shift().split(' ').map(e=>parseInt(e));

for(var i=n; i<=m; i++) 
    isPrime(i) ? console.log(i) : null; 

// const [n,m] = input.shift().split(' ').map(e=>parseInt(e));
// const arr = Array.from(Array(m+1).keys())
// for(let i=2; i<=Math.sqrt(m); i++){
//     if(arr[i])
//         for(let j = i*i; j<=m; j+=i)
//             arr[j] = false;
// }
// arr.splice(0,2,false,false)
// for(let i = n; i<=m; i++){
//     // console.log(arr[i])
//     if(arr[i]) console.log(arr[i])
// }