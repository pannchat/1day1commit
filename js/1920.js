let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = parseInt(input.shift())
const arr = new Set(input.shift().split(' '));
const M = parseInt(input.shift())
const arrM = input.shift().split(' ');
arrM.map( e => {arr.has(e) ? console.log(1) : console.log(0)})




// arr.sort();

// arrM.map(e => {
//     let l = 0;
//     let r = arr.length;
//     let res=0; 
//     while(l<=r){
//         let mid = parseInt((l+r)/ 2);     

//         if(e === arr[mid]){
//             res=1;
//             break;
//         }else if(e<arr[mid]){
//             r=mid-1;
            
//         }else{
//             l=mid+1;
//         }
        
//     }
//     console.log(res);
// })



// arrM.map( e => {arr.includes(e) ? console.log(1) : console.log(0)})



// const N = parseInt(input.shift())
// const arr = new Set(input.shift().split(' '));
// const M = parseInt(input.shift())
// const arrM = input.shift().split(' ');
// arrM.map( e => {arr.has(e) ? console.log(1) : console.log(0)})

// arr.sort();
// //---------
// arrM.map(e => {
//     let l = 0;
//     let r = arr.length;
//     let res=0; 
//     while(l<=r){
//         let mid = parseInt((l+r)/ 2);     

//         if(e === arr[mid]){
//             res=1;
//             break;
//         }else if(e<arr[mid]){
//             r=mid-1;
            
//         }else{
//             l=mid+1;
//         }
        
//     }
//     console.log(res);
// })

