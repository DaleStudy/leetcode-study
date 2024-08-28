/**
 * TC: O(n)
 * SC: O(n)
 */
function numDecodings(s: string): number {
  const n = s.length;
  const dp = new Array(n + 1).fill(0);

  dp[0] = 1;
  dp[1] = Number(s[0]) === 0 ? 0 : 1;

  for (let i = 2; i <= n; i++) {
    const oneDigit = Number(s.slice(i - 1, i));
    const twoDigits = Number(s.slice(i - 2, i));

    if (oneDigit >= 1 && oneDigit <= 9) {
      dp[i] += dp[i - 1];
    }

    if (twoDigits >= 10 && twoDigits <= 26) {
      dp[i] += dp[i - 2];
    }
  }

  return dp[n];
}
