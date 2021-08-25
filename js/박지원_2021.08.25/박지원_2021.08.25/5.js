const heights = [4,2,6,9,14,12];
// const heights = [14,3,19,3];
// 반례
// const heights = [1,4,7,14,15,18]
const bricks = 5;
const ladders = 1;
const jump = (heights, bricks, ladders) =>{
    for(const [i,el] of heights.entries()){
        // console.log(el)
        if(bricks +ladders <= 0) return i;
        const nextValue = heights[i+1] ?? false; // 다음값 없으면 false  
        if(nextValue){ // 다음 값이 있으면
            if(el < nextValue){
                
                if(nextValue-el<=bricks){

                    bricks -= nextValue - el;

                }else{
                        ladders--;

                    
                }
            }

        }
    }
    return heights.length-1;



}

console.log(jump(heights,bricks,ladders))