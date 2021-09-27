let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = parseInt(input.shift())

for(let i=0; i<T; i++){
    let count = 0;
    const [n,m,k] = input.shift().split(' ').map(e=>+e);
    const arr = Array.from(Array(n), ()=>new Array(m).fill(false));
    const check = Array.from(Array(n), ()=>new Array(m).fill(false));

    for(let j=0;j<k;j++){
        const [x,y] = input.shift().split(' ').map(e=>+e);
        arr[x][y] = true;
    }
    for(let a=0; a<n; a++){
        for(let b=0; b<m; b++){
            if(arr[a][b]){
                bfs(a,b);
                count++;
            }
        }
    }

    function bfs(x,y){
    

        const dx = [1,0,-1,0];
        const dy = [0,-1,0,1];
        const queue = [[x,y]];
        while(queue.length!==0){
            const [a,b] = queue.shift()
            arr[a][b] = false
            for(let i =0; i<4; i++){
                let xx = dx[i]+a;
                let yy = dy[i]+b;
                if(0<=xx && xx <n && 0<=yy && yy <m){
                    if(arr[xx][yy]){
                        arr[xx][yy] = false;
                        queue.push([xx,yy])
                    }
                }
            }
        }
        
        
    }
    console.log(count)
}


