let data = {
    'key1':[1,2,3],
    'key2':[{'key':'value'}],
    'key3':[4,5,6]
}

let test2 = data;
console.log(data)
console.log(test2)
// data['key3']= data['key3'].filter(e=>e>5);
data = {
    ...data,
    'key3': data['key3'].filter(e=>e>5)
}
// let test = {
//     ...data,
//     'key3': data['key3'].filter(e=>e>5)
// }
console.log(data)
console.log(test2)

// console.log(test)
// console.log(data===test)