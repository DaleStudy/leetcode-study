// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  const n = nums.length;
  const dp = Array.from({ length: n + 1 }, () => Number.MIN_SAFE_INTEGER);
  dp[0] = 0;

  for (let i = 1; i <= n; i++) {
    dp[i] = Math.max(dp[i - 1] + nums[i - 1], nums[i - 1]);
  }

  return Math.max(...dp.slice(1));
};
