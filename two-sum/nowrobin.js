/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// 34ms 54mb
var twoSum = function(nums, target) {
        for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[j] === target - nums[i]) {
                return [i, j];
            }
        }
    }
    return []
};
