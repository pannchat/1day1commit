// target = 'abc';
// words = ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'];
target = 'cloud';
words = ['card', 'cd', 'lol', 'doc'];
const findFunc = (target, words) =>{
    let count = 0;
    for(word of words){
        let pass = true
        for(el of word){
            if (!target.includes(el)) pass=false;
        }
        if(pass)count++;
    }
    return count;
}

console.log(findFunc(target,words));