
function solution(numbers) {
    var answer = [];
    const arr = []
    let ans = numbers.map( num =>{
        let sum =0;
        for(let i = 1; i*i<=num;i++){
            if(i*i == num){
                sum+=i
            }else if(num%i === 0){
                sum += i+num/i;
            }
        
        }
        
        return sum;
    })
    console.log(ans)

    // for(let i = 1; i<=numbers.length; i++ ){
    //     let sum = 1+i
    //     for(let j = 2; j<i ; j ++){
    //         if(i % j === 0){
    //            console.log(numbers[j-1])
    //            sum+=numbers[j-1] 
    //         }
    //     }
    //     answer.push(sum)
    //     console.log('-----')
    // }

    // console.log(answer)
    // return answer;
}

solution([1,2,3,4,5,6])