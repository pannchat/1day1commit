const { throws } = require('assert');
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
dx = [1,0];
dy = [0,1];

const n = parseInt(input.shift());
const arr = [];


class Node{
    constructor(data){
        this.data=data;
        this.next = null;
        this.prev = null;
    }
}

class LinkedList{
    constructor(){
        this.head = null;
        this.tail = null;
        this._size = 0;
    }
    enqueue(data){
        
        const newNode = new Node(data);

        if(!this.head)
            this.head = newNode;
        else{
            this.tail.next = newNode
            newNode.prev = this.tail
        }

        this.tail = newNode
        this._size++;

        return newNode;
    
    }
    dequeue(){
        let temp = this.head.data;
        this.head = this.head.next;
        // this.head.prev = null;
        this._size--;
        return temp;
    }
    
    length(){
        return this._size;
    }
}
for(let i=0; i<n;i++){
    arr.push(input.shift().split(' ').map(e=>+e))
}
const check = new Array(n);
for(let i=0;i<n;i++){
    check[i] = new Array(n).fill(false)
}
const queue = new LinkedList();
queue.enqueue([0,0])


check[0][0]=true
while(queue.length()!==0){

    const [x,y] = queue.dequeue();
    if(arr[x][y] == -1){
        return console.log('HaruHaru');
    }
    for(let i =0; i<2; i++){
        
        let xx = dx[i]*arr[x][y]+x;
        let yy = dy[i]*arr[x][y]+y;

        if(0<=xx && xx<n && 0<=yy && yy<n ){
            if(!check[xx][yy])
                check[xx][yy] = true
                queue.enqueue([xx,yy])


        }
    }
    
}

return console.log("Hing");

    




// console.log('Hing')
