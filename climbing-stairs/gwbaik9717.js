// Time complexity: O(n)
// Space complexity: O(n)

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  const dp = Array.from({ length: n + 1 }, () => 0);
  dp[0] = 1;
  dp[1] = 1;

  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
};
