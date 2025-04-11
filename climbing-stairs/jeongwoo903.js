/*
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
  if (n === 1) return 1;

  const dp = [1, 2]

  for (let i = 2; i < n; i++) {
    dp[i] = dp[i-1] + dp[i-2]
  }

  return dp[n-1]
};
