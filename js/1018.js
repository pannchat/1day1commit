let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let min = 100;
let res = [];
const [n,m] = input.shift().split(' ');

let board = input.map( el => Array.from(el));

console.log(board)
const [black_board,white_board] = (()=>{
    return [Array.from('BWBWBWBWWBWBWBWB'),Array.from('WBWBWBWBBWBWBWBW')];
})();
// console.log(black_board)

for (var i=0; i<n-8; i++){
    for(var j=0; j<m-8; j++){
        var b_cnt=0;
        var w_cnt=0;
        board.map((el,i) => {
            black_board.slice(i,i+1)
        })
    }

    // res.push(b_cnt,w_cnt);
    // console.log(b_cnt)
}
// console.log(Math.min(...res))