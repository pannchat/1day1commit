// const matrix = [[1,2,3],[4,5,6],[7,8,9]];
// const matrix = [[1,1,1,2],[1,1,1,1],[1,1,1,1],[1,1,1,2]];
const matrix = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]];
// const matrix = [[1,2],[3,4]];
// const matrix = [[1]];
const matrixSum = (matrix) =>{
    const n = matrix.length;
    let sum = 0;
    
    for(let i = 0; i<n; i++){
        sum += matrix[i][i];
        sum += matrix[i][n-i-1];
    }
    return n%2===0 ? sum : sum-matrix[parseInt(n/2)][parseInt(n/2)]
}
console.log(matrixSum(matrix))