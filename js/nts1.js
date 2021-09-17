function solution(votes, k) {
    var answer = '';
    const car= {};
    const carArr = [];
    votes.forEach( e=>{
        if(!car[e]) car[e] = 1;
        else car[e]++;
    })
    Object.keys(car).forEach(e=>{
        carArr.push([e,car[e]])
    })

    carArr.sort((a,b) => {
        if(b[1] === a[1]) 
            return a[0] > b[0] ? 1 : -1
        else 
            return b[1]-a[1]
    })
    let sum = 0
    let temp = 0;
    for(let i=0; i<k; i++){
        const [name,vote] = carArr[i]
        sum += vote;
    }

    while(sum>0){
        const [name, vote] = carArr.pop()

        if(sum <= vote){
            return temp;
        }else{
            sum -= vote;
            temp = name;
        }

    }
    return answer;
}