/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length === 0) return 0;
  if (nums.length === 1) return nums[0];

  const dp = new Array(nums.length + 1);
  dp[0] = 0;
  dp[1] = nums[0];
  for (let i = 2; i < dp.length; i++) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i - 1]);
  }
  return dp[dp.length - 1];
};

const nums = [2, 7, 9, 3, 1];

console.log(rob(nums));
