/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const numsMap = {};

    for (let i = 0; i < nums.length; i++) {
        const needNum = target - nums[i];

        if (needNum in numsMap) {
            return [i, numsMap[needNum]];
        }

        numsMap[nums[i]] = i;
    }
};
