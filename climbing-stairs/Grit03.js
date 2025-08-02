/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  const dp = [0];

  for (let i = 1; i <= n; i++) {
    if (i === 1) {
      dp[1] = 1;
      continue;
    }
    if (i === 2) {
      dp[2] = 2;
      continue;
    }
    dp[i] = dp[i - 2] + dp[i - 1];
  }
  return dp[n];
};
