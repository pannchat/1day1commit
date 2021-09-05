
var containsDuplicate = function(nums) {
    let newArr = new Set(nums);
    return newArr.size !== nums.length
};

