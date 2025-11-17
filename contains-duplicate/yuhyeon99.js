/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let numsSet = new Set();
    for(let i = 0; i < nums.length; i ++) {
        if(numsSet.has(nums[i])) return true;
        numsSet.add(nums[i])
    }
    return false;
};
