let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = parseInt(input.shift());
const arr = []
for(let i = 0; i < n; i++){
    arr.push(parseInt(input.shift()));
}

// 산술평균
console.log(Math.round(arr.reduce( (a,b) =>a+b,0)/n));
arr.sort((a,b) => a-b);
// 중앙값
console.log(arr[parseInt(n/2)])
//최빈값
const dict = new Map();
arr.forEach(e=>{
    if(dict.has(e)) dict.set(e,dict.get(e)+1)
    else dict.set(e,1);
})
let max = 0;
let checkArr = [];

for(let value of dict.keys()){
    if(max < dict.get(value))
        max = dict.get(value);
}

for(let value of dict.keys()){
    if(max === dict.get(value)){
        checkArr.push(value)
    }
}
console.log(checkArr.length > 1 ? checkArr[1] : checkArr[0])

console.log(Math.abs(arr[n-1] - arr[0]));