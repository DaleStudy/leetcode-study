// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  const n = nums.length;
  const dp = Array.from({ length: n + 1 }, () => 0);
  dp[1] = nums[0];

  for (let i = 2; i < n + 1; i++) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i - 1]);
  }

  return dp.at(-1);
};
