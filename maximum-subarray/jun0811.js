/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  const dp = [nums[0]];
  for (let i = 1; i < nums.length; i++) {
    const cur = nums[i];
    if (dp[i - 1] < 0) dp[i] = cur;
    else {
      dp[i] = dp[i - 1] + cur;
    }
  }
  return Math.max(...dp);
};
