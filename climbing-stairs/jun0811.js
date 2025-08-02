/**
 * @param {number} n
 * @return {number}
 */

// Time Complexity : O(N)
var climbStairs = function (n) {
  if (n == 1) return 1;
  if (n == 2) return 2;

  const dp = [1, 2];

  for (let i = 2; i < n; i++) {
    dp[i] = dp[i - 2] + dp[i - 1];
  }
  return dp[n - 1];
};
