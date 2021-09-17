let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n,m] = input.shift().split(' ').map(e=>parseInt(e));
const arr = [];
for(let i=0; i<n; i++){
    arr.push(input.shift().split('').map(e=>parseInt(e)))
}
const check= Array.from(Array(n), ()=>new Array(m).fill(false));

const res = []
const dx = [1, 0, -1, 0];
const dy = [0,-1,0,1];

class Queue{
    constructor(){
        this._arr = [];
    }
    enqueue(value){
        this._arr.push(value);
    }
    dequeue(){
        return this._arr.shift()
    }
    length(){
        return this._arr.length;
    }
    isEmpty(){
        return this._arr.length === 0 
    }
}



const BFS = (startV) => {
    const queue = new Queue();
    queue.enqueue(startV);
    check[0][0] = true;
    while(!queue.isEmpty()){
            const [x,y,cnt] = queue.dequeue();
            for(let j =0; j<4; j++){
                const xx = x + dx[j];
                const yy = y + dy[j];
                
                if(0<=xx && xx < n && 0<= yy && yy < m ){
                    if(!check[xx][yy] && arr[xx][yy] === 1){        
                            arr[xx][yy] = cnt + 2;
                            queue.enqueue([xx,yy,cnt+1])              
                    }
                }
            }
        }
    }

BFS([0,0,0])
console.log(arr[n-1][m-1])
// const DFS = (x,y,cnt) =>{
    
//     if(x === n-1 && y === m-1){
//         res.push(++cnt);
//         return
//     }

//     for(let i=0; i<dx.length; i++){
//         let xx = x + dx[i];
//         let yy = y + dy[i];

//         if (0<=xx && xx<n && 0<=yy && yy<m){

//             if(check[xx][yy] === false && arr[xx][yy]===1){
//                 check[x][y] = true;
//                     DFS(xx,yy,++cnt);
//                     check[x][y] = false;
//                     --cnt;
//             }
//         }

//     }
// }

// DFS(0,0,0)
// console.log(Math.min(...res))