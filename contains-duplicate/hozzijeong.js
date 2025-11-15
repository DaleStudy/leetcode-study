/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const originLength = nums.length;
    const numsSet = new Set(nums);

    return originLength !== numsSet.size;
};
