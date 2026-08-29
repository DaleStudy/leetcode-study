function numDecodings(s) {
  const dp = Array.from({ length: s.length + 1 }, () => 0);
  dp[0] = 1;
  dp[1] = s[0] === '0' ? 0 : 1;
  for (let i = 2; i <= s.length; i++) {
    if (s[i - 1] !== '0') {
      dp[i] += dp[i - 1];
    }

    const twoDigits = Number(s.slice(i - 2, i));
    if (twoDigits >= 10 && twoDigits <= 26) {
      dp[i] += dp[i - 2];
    }
  }
  return dp[s.length];
}
