// Time complexity: O(n)
// Space complexity: O(1)

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  const dp = [1, 1];

  for (let i = 2; i <= n; i++) {
    dp[i % 2] = dp[0] + dp[1];
  }

  return dp[n % 2];
};
