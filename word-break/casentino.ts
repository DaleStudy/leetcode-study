function wordBreak(s: string, wordDict: string[]): boolean {
  const dp = new Array(s.length + 1).fill(false);
  dp[0] = true;
  for (let i = 1; i <= s.length; i++) {
    let str = "";
    for (let j = 0; j < wordDict.length; j++) {
      let start = i - wordDict[j].length;
      if (start >= 0 && dp[start] && s.substring(start, i) === wordDict[j]) {
        dp[i] = true;
        break;
      }
    }
  }
  return dp[s.length];
}
