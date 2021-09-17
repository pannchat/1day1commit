function solution(N, K, charges) {
    var answer = [];
    const arr = new Array(N).fill(0);
    let res = 0
    charges.forEach((e,i)=>{
        // console.log(i)
        if(i===K-1){
            res = arr.indexOf(Math.min(...arr));

        }

        arr[arr.indexOf(Math.min(...arr))] += e;
    })
    return [res+1,arr[res]];
}