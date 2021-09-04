
 var twoSum = function(nums, target) {
    const map={};
   for(let i = 0; i<nums.length; i++){
       const value = target - nums[i];
       if(nums[i] in map)
           return [map[nums[i]],i];
        map[value] = i
   }

};