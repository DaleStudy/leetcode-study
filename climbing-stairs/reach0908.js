/**
 * @description
 * time complexity: O(n)
 * space complexity: O(n)
 * runtime: 0ms
 * 풀이 방법: 기본적인 DP 풀이 방법
 * @param {number} n
 * @return {number}
 */
const climbStairs = function (n) {
  const dp = [1, 2];

  for (let i = 2; i < n; i += 1) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n - 1];
};
