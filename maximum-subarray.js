const arr = []
let max = -2147483600;
for(let i=0; i<nums.length; i++){
    let sum = 0
    for(let j=i; j<nums.length; j++){
        sum+=nums[j]
        max = Math.max(max,sum);
    }
    
}

return max;

var maxSubArray = function(nums) {
    let max = -2147483640;
    let partialSum = 0;
    for(let i=0; i<nums.length; i++){
      partialSum = Math.max(0,partialSum) + nums[i];
      max = Math.max(partialSum, max)
    }
    return max;
};
