let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const word = input.shift();
const digit = [];
const str = [];

const reconstructor = (param1,param2) => {
    let p1 = [...param1];
    let p2 = [...param2];
    let ans = '';
    for(let i = 0; i<word.length; i++){
        i%2 === 0 
        ? ans += p1.shift() 
        : ans += p2.shift() 
    }
    return ans;
}

for( el of word ){
    if(isNaN(el)) str.push(el);
    else digit.push(el)
};
let len = digit.length - str.length;

if(Math.abs(len) > 1) return console.log("")
else if(len === 0){ // 같다면 같은 출력을 제외하고 다른 조합을 출력
    reconstructor(digit, str) === input 
    ? console.log(reconstructor(str,digit))
    : console.log(reconstructor(digit, str))
    
    
}
else if(len > 0)  // digit이 더 크다면
    console.log(reconstructor(digit, str));
else
    console.log(reconstructor(str,digit));

