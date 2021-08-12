let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n,k] = input.shift().split(' ');
let l=1, r = Math.max(...input);
let res=0;
const cutting = (cm) =>{
    return( input.reduce((s, cable) => {
        return s + parseInt(cable/cm)
    },0));
    
}

while(l<=r){
    var mid = parseInt((l+r)/2)

    var lan = cutting(mid);

    if(k<=lan){
        res = mid
        l=mid+1
        
    }else{
        r=mid-1;
    }
    
}
console.log(res)

