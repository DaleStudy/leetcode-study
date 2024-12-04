/**
 * @param {number[]} nums
 * @return {boolean}
 */

var containsDuplicate = function(nums) {
    const duplicate = new Set();

    for (let i = 0; i < nums.length; i++) {
        if (duplicate.has(nums[i])) {
            return true;
        }
        duplicate.add(nums[i]);
    }

    return false;
};
