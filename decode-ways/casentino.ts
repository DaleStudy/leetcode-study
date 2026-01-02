function numDecodings(s: string): number {
  if (s.length === 1 && s[0] !== "0") {
    return 1;
  }
  if (s[0] === "0") {
    return 0;
  }
  const dp = new Array(s.length + 1).fill(0);
  dp[0] = 1;
  dp[1] = 1;
  for (let i = 2; i <= s.length; i++) {
    if (s[i - 1] !== "0") {
      dp[i] += dp[i - 1];
    }
    const doubleNum = parseInt(s[i - 2] + s[i - 1]);
    if (doubleNum >= 10 && doubleNum <= 26) {
      dp[i] += dp[i - 2];
    }
  }
  return dp[s.length];
}
