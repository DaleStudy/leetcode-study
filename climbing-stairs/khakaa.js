/**
 * Complexity:
 * - Time: O(n)
 * - Space:	O(n)
 */

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let dp = Array.from({ length: n + 1 });

  dp[0] = 1;
  dp[1] = 1;

  if (n === 1) return dp[1];

  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
};
