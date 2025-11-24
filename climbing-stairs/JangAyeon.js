/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  const dp = [0, 1, 2];
  for (let i = 3; i <= n; i++) {
    const value = dp[i - 2] + dp[i - 1];
    dp.push(value);
    // console.log(i, value)
  }

  return dp[n];
};
