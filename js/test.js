// // let arr = [1,1,4,6,4,2,4,5,5,7]
// // let test = new Map();


// // arr.map(e=>{
// //     if(test.has(e)){
// //         test.set(e, test.get(e)+1)
// //     }else{
// //         test.set(e,1);
// //     }
// // })

// // console.log(new Map([...test.entries()].sort((a,b)=>a[0]-b[0])))

// let arrs = [[360, 138, 338], [230, 102, 311], [320, 474, 214], [131, 498, 484], [366, 176, 249], [323, 407, 116], [265, 433, 317]]
// let arr = []
// arrs.forEach(e=>{
//     arr = arr.concat(...e);
// })

// const dp = [arr[0],arr[1],arr[2]];
// let i =3;
// while( i< arr.length){
//     dp[i] = Math.min(dp[i-1],dp[i-2],dp[i-3])+arr[i]
//     i++
// }
// console.log(dp)

let dx = [0,1,0,-1]
let dy = [1,0,-1,0]

function bfs(x,y,map,check){
    const queue = [[x,y]]
    let cnt = new Map();
    const n = map[0].length;
    const m = map.length;
    while(queue.length!==0){
        const [x,y] = queue.shift()
        check[x][y] = true;
        for(let i=0; i<4; i++){
            let xx = dx[i] + x;
            let yy = dy[i] + y;
            if(0<= xx && xx < n && 0<=yy && yy < m){
                if(map[xx][yy] !== '.' && check[xx][yy] === false){
                    const e = map[xx][yy];
                    if(cnt.has(e)){
                        cnt.set(e,cnt.get(e)+1)
                    }else{
                        cnt.set(e,1)
                    }
                    queue.push([xx,yy])
                }

            }
        }
    }
    console.log(x,y)
    console.log(cnt)
    let res = [...cnt.entries()].sort((a,b) => {
        if(a[1]-b[1] === 0 ){
            return a[0] - b[0]
        }else{
            return b[1] - a[1]
        }
    })
    console.log(res[0][1])
    // return res[0][0]
}

function solution(maps){
    var answer = 0;
    const map = maps.map(e=>{
        return e.split('')
    })
    const check = Array.from(Array(map.length), ()=>new Array(map[0].length).fill(false) )
    for(let i=0; i<map.length; i++){
        for(let j=0; j<map[0].length; j++){

            if(check[i][j] === false && map[i][j] !== '.'){
                
                bfs(i,j,map,check)
            }
        }
    }
}

solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"])