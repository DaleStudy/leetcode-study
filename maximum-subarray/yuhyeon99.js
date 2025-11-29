/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxSum = nums[0];
    let sum = 0;
    nums.forEach((num) => {
        sum = Math.max(sum + num, num);
        maxSum = Math.max(sum, maxSum);
    });
    return maxSum;
};
