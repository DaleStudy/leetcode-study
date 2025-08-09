function climbStairs(n: number): number {
  const dp: number[] = Array.from({ length: n + 1 }, () => 0);
  dp[0] = 1;
  dp[1] = 1;

  for (let i = 2; i < n + 1; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}
