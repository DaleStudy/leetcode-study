// T.C: O(n)
// S.C: O(n)

function climbStairs(n: number) {
  const dp = { 1: 1, 2: 2 };
  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  return dp[n];
}
