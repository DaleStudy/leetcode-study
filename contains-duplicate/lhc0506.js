/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const numsSet = new Set();
    nums.forEach(num => numsSet.add(num));

    return nums.length !== numsSet.size;
};
