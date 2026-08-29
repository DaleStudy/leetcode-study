/**
 * 시간 복잡도: O(n)
 * 공간 복잡도: O(n)
 */
function numDecodings(s: string): number {
  const dp = new Array(s.length + 1).fill(0);
  dp[0] = 1;
  dp[1] = parseInt(s[0]) === 0 ? 0 : 1;

  for (let i = 2; i <= s.length; i++) {
    dp[i] = 0;

    if (parseInt(s[i - 1]) !== 0) {
      dp[i] += dp[i - 1];
    }
    if (
      parseInt(s.slice(i - 2, i)) <= 26 &&
      parseInt(s.slice(i - 2, i)) >= 10
    ) {
      dp[i] += dp[i - 2];
    }
  }
  return dp[s.length];
}
