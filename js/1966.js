let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const max = (arr) => {
    let arr2 = arr.map(e=>e[0])
    return Math.max(...arr2);
}


n = parseInt(input.shift())
for(let i = 0; i<n; i++){
    let cnt = 1;
    const [nn,findIdx] = input.shift().split(' ');

    const arr = input.shift().split(' ').map( (e,i)=>{
        return [parseInt(e),i];
    })
    const findIt = arr[findIdx];

    while(true){

        if(max(arr)===arr[0][0] && arr[0] ===findIt){

            break;
        }else if(max(arr)===arr[0][0]){
            arr.shift();
            cnt++;
        }else{
            arr.push(arr.shift())
        }
    }
    console.log(cnt)
    
}
