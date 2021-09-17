function solution(numbers) {
    var answer = [];
    const arr = []
    for(let i = 1; i<=numbers.length; i++ ){
        let sum = 0
        for(let j = 1; j<=i ; j ++){
            if(i % j === 0){
               sum+=numbers[j-1] 
            }
        }
        answer.push(sum)
    }
    console.log(answer)
    return answer;
}