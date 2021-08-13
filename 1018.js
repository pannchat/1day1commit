let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n,m] = input.shift().split(' ');

const board = input.map( el => Array.from(el));
console.log(board);

// const [black_board,white_board] = (()=>{
//     return [Array.from('BWBWBWBWWBWBWBWB'.repeat(4)),Array.from('WBWBWBWBBWBWBWBW'.repeat(4))];
// })();


console.log(black_board)