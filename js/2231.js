let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

function find(){
    const n = parseInt(input.shift());
    const arr = new Array(n).fill(false);
    for(let i = 1; i<=parseInt(n);i++){
        let sum=0;
        String(i).split('').map(e=>{
            sum+= +e;
        })
        sum+=i
        if(sum === n) return i;
        // if(!arr[sum]) arr[sum] = i;
    }
    return 0;
}

console.log(find())
