
class Stack{
    constructor(){
        this.data = []
        this.top = 0;
    }

    push(element) {
        this.data[this.top] = element;
        this.top += 1;
    }
    pop(){
        if(this.isEmpty() === false){
            this.top = this.top -1 ;
            return this.data.splice(-1)[0];
        }
    }
    isEmpty(){
        return this.top === 0;
    }


}

const solution = () => {
    let n = parseInt(input.shift());
    let cnt = 0;
    let stack = new Stack();
    let answer = '';
    for(e of input){
        while(e > cnt){
            stack.push(++cnt);
            answer += "+\n";
        }
        if(stack.pop() !== e){
            return "NO";
        }
        answer += "-\n";
    };
    return answer;
}

let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(e=>parseInt(e));
console.log(solution(input));



