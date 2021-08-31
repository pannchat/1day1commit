function bubble(arr){
    for(let i = 0; i<arr.length; i++){
        for(let j=0; j<arr.length-1-i; j++){
            if(arr[j]>arr[j+1]){
                 [arr[j],arr[j+1]] = [arr[j+1],arr[j]]
            }
        }
    }
    return arr;
}
console.log(bubble([4,2,3,1]))


// function selection(arr){
//     for(let i =0; i<arr.length; i++){
//         let min = i;
//         for(let j=i+1; j<arr.length; j++){
//             if(arr[min]>arr[j]) min=j;
//         }
//         [arr[i],arr[min]] = [arr[min],arr[i]]
//     }
//     return arr;
// }

function selection(arr){
    for(let i=0; i<arr.length; i++){
        let min = i;
        for(let j=i+1; j<arr.length; j++){
            if(arr[min]>arr[j]) min = j;
        }
        [arr[min],arr[i]] = [arr[i],arr[min]]
    }
    return arr;
}
console.log(selection([4,2,3,1]))

function insertion(arr){
    for(let i=1; i<arr.length; i++){
        let j = i
        while(arr[j-1] > arr[j]){
            [arr[j-1],arr[j]] = [arr[j],arr[j-1]];
            j--;
        }
        
    }
    return arr;
}
console.log(insertion([4,2,3,1]))