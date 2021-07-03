function solution(n) {
    var answer = ''
    var arr=[4,1,2]
    while(n>0){
        
        answer = arr[n%3] + answer 
        if(n%3 == 0)
            n = parseInt(n/3) -1
        else
            n = parseInt(n/3)
    }
    return answer;
}
 