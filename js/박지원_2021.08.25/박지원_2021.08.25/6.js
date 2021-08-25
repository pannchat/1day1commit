// 벨트 -> 슬롯 -> 인력 ? 차 : 벨트
const slot = { //최대 200
    'A':0,
    'B':0,
    'C':0,
    'D':0,
    'E':0,
    'F':0
}
let car = {
    'A':[0,0],
    'B':[0,0],
    'C':[0,0],
    'D':[0,0],
    'E':[0,0],
    'F':[0,0]
}
const slotElement = ['A','B','C','D','E','F'];
let belt = 0;
let time = 0; //분단위
let man = 2; // 차량에 물건을 싣는 인력 수

const sum = (obj) =>{ 
    return Object.keys(obj).reduce((sum,key)=>sum + parseFloat(obj[key]||0),0);
}

while( sum(slot) +belt < 10000 ){
    if(time%60===0 || time===0) belt += 2000;
    if(sum(slot) +belt >= 10000) break;

    slotElement.forEach((el)=>{
        let product = 200 - slot[el];
        if (belt - product > 0){
            //벨트에 제품이 있으면?
            slot[el] += product
            belt -= product;
        }else{
            // 없으면 대기
            // console.log('대기')
        }
    });
    slotElement.forEach((el)=>{
        const [wait,stack] = car[el];
        if(car[el][0]===0) //배차대기중이 아니라면
            if(wait===0 && (stack===150 || slot[el]===0 )){ //출발할 때 됐는지
                car[el][1]=0;
                car[el][0]=10;
            }else{
                for(let i =0; i<man*6; i++){
                    if(slot[el] && stack!==150){
                        slot[el]--;
                        car[el][1]++;
                    }
                }
              
            }
        else{
            // console.log('차량 대기', car[el][0],'분')
            car[el][0]--;
        }
    })
    console.log(sum(slot),belt,time)
    
    time++;
}

console.log('차량에 물건을 싣는 인력이', man,'명인 경우', time/60,'시간 후에 멈춥니다.')


/* 

1.1. 처리가 가능한 물류량인가?
 - 처리가 불가능합니다. 약 25600개 이후부터 컨베이어벨트의 가동이 멈추게됩니다.
1.2. 멈출 수 밖에 없는 물류량이라면 그것은 운영을 시작한 후 언제가 될까?
 - 17시간 후에 멈추게 됩니다.

2. 멈추지 않고 운영할 수 있도록 알고리즘이나 해결책을 제시하세요
- 차량에 물건을 싣는 인력을 1명씩 늘리면 됩니다.
let man = 2로 실행하였을때 멈추지 않고 계속진행되었습니다.
 */
