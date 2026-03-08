/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let maxSum = nums[0];
  let max = nums[0];

  for (let i = 1; i < nums.length; i++) {
    max = Math.max(nums[i], max + nums[i]);
    maxSum = Math.max(max, maxSum);
  }
  return maxSum;
};
