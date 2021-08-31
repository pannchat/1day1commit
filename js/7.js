function fac(n){
    if (n===1) return 1;
    else return n* fac(n-1)
}

console.log(fac(4));

function fibo(n){
    if(n<2) return n;
    else return fibo(n-1) + fibo(n-2);
}

console.log(fibo(4))

class Stack{
    constructor(){
        this.arr=[];
        this.top=0;
    }
    push(item){
        this.arr[this.top++] = item;
    }
    pop(){
        if(this.top <= 0) return null;
        let temp = this.arr[--this.top];
        delete this.arr[this.top]
        return temp;
    }

}

let stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.arr);
