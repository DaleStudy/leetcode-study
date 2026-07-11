/**
 * 시간 복잡도 O(n)
 * 공간 복잡도 O(n)
 */
function climbStairs(n: number): number {
  // NOTE: n이 1일 경우 바로 종료
  if (n === 1) return 1;

  const dp = new Array(n).fill(0);

  dp[0] = 1;
  dp[1] = 2;

  for (let i = 2; i < dp.length; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[dp.length - 1];
}
