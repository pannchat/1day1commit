function solution(answers) {
    var answer = [];
    const supoList = [0,0,0];
    const supo1 = [1,2,3,4,5];
    const supo2 = [2,1,2,3,2,4,2,5];
    const supo3 = [3,3,1,1,2,2,4,4,5,5]
    answers.forEach((e,i)=>{
        console.log(e,supo1[i%5])
        if(supo1[i%5] === e) supoList[0]++;
        if(supo2[i%8] === e) supoList[1]++;
        if(supo3[i%10] === e) supoList[2]++;
    })
    supoList.forEach((e,i)=>{
        if(e === Math.max(...supoList)) answer.push(i+1);
    });

    return answer;
}
