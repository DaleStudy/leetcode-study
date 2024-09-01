const climbStairs = function (n) {
  const dp = [1, 1];

  for (let i = 0; i < n - 1; i++) {
    const temp = dp[1];
    dp[1] = temp + dp[0];
    dp[0] = temp;
  }

  return dp[1];
};
