const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, m] = input.shift().split(' ').map( (el) => parseInt(el));
const chk = Array.from(Array(n), () => new Array(m).fill(false));
const arr = []
input.map((line)=>{
    arr.push(line.split(' '));
})
// arr.pop()

function outRange(x,y){
    return 0<=x && x < n && 0 <= y && y < m;
}

const d = [[0,1],[-1,0], [0,-1], [1,0]];
const bfs = (x,y) =>{
    let count = 1;
    

    const q = [];
    chk[x][y] = true;
    q.push([x,y]);
    while(q.length){
        let len = q.length;
        while(len--){
            [x,y] = q.shift();
            d.forEach(v => {
                const [xx,yy] = v;
                
                const [nx,ny] = [x + xx, y + yy];
                if(!outRange(nx,ny) || chk[nx][ny] || arr[nx][ny] === '0') return;
                q.push([nx,ny]);
                count++;
                chk[nx][ny] = true;
            })
        }
    }
    return count;
}
let res = []
for(var i=0; i< n; i++){
    for(var j=0; j<m; j++){
        if(!chk[i][j] && arr[i][j]==='1'){
            res.push(bfs(i,j));
        }
    }
}
    console.log(res.length);
    if (res.length === 0 ){
        console.log(0)
    }else{
        console.log(Math.max(...res))
    }
    

