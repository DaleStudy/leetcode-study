/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const sortedNums = nums.sort((a, b) => a - b);
    const length = sortedNums.length - 1;

    for (let i = 0; i < length; i++) {
        const left = nums[i];
        const right = nums[i + 1];

        if (left === right) {
            return true;
        }
    }

    return false;
};
