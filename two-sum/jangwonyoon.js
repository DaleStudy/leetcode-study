/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const length = nums.length - 1;

    for (let i = 0; i < length; i++) {
        for (let j = length; j > 0; j--) {
            const sum = nums[i] + nums[j];

            if (sum === target) {
                return [i, j];
            }
        }
    }
};