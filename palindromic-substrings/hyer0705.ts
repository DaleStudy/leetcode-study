function countSubstrings(s: string): number {
  const sLen = s.length;

  const dp: boolean[][] = Array.from({ length: sLen }, () => Array(sLen).fill(false));

  // 길이가 1
  for (let i = 0; i < sLen; i++) {
    dp[i][i] = true;
  }

  // 길이가 2
  for (let i = 0; i < sLen - 1; i++) {
    dp[i][i + 1] = s[i] === s[i + 1];
  }

  // 길이가 3이상
  for (let len = 3; len <= sLen; len++) {
    for (let i = 0; i < sLen - len + 1; i++) {
      const j = i + len - 1;
      if (s[i] === s[j] && dp[i + 1][j - 1]) {
        dp[i][j] = true;
      }
    }
  }

  let count = 0;
  for (let i = 0; i < dp.length; i++) {
    for (let j = 0; j < dp[i].length; j++) {
      if (dp[i][j]) count++;
    }
  }

  return count;
}
