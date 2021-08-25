let array = [1,4,2,5,3]
const arraySum = (array=[1,4,2,5,3]) =>{

    let n = array.length;
    let sum = array.reduce( (sum,cur,i) => {
        let odd = parseInt(((i+1)*(n-i) +1)/2); //홀수만
        return sum + (odd * array[i]);
    },0 )

    return sum;
}

console.log(arraySum(array))