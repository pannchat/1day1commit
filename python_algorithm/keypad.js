function dist(e, lr){
    return Math.abs(lr[0]-e[0]) + Math.abs(lr[1]-e[1])
    
}
function solution(numbers, hand) {
    var answer = '';
    var l=[3,0];
    var r=[3,2];
    var keypad ={
        1:[0,0], 2:[0,1], 3:[0,2],
        4:[1,0], 5:[1,1], 6:[1,2],
        7:[2,0], 8:[2,1], 9:[2,2],
        '*':[3,0], 0:[3,1], '#':[3,2]
    } 

    numbers.map( e=> {
        if (keypad[e][1] === 0){
            answer+='L'
            l = keypad[e]
        }else if(keypad[e][1] === 2){
            answer+='R'
            r = keypad[e]
        }else{
            if (dist(keypad[e],l) === dist(keypad[e],r)){
                if(hand === 'right'){
                    answer+='R';
                    r = keypad[e]
                }else{
                    answer+='L'; 
                    l = keypad[e];
                }  
            }
            else if(dist(keypad[e],l) > dist(keypad[e],r)){
                   answer+='R';
                r = keypad[e]
            }else{
                answer +='L'
                l = keypad[e]
            }
        }
    })
    console.log(answer);
    return answer;
}
