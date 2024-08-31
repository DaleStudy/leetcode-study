/**
 * @description
 * brainstorming:
 * Dynamic Programming
 *
 * time complexity: O(n)
 * space complexity: O(n)
 */

var climbStairs = function (n) {
  const dp = Array.from({ length: n + 1 }, () => 0);
  dp[1] = 1;
  dp[2] = 2;

  for (let i = 3; i < n + 1; i++) dp[i] = dp[i - 1] + dp[i - 2];

  return dp[n];
};
