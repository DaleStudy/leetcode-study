var longestCommonSubsequence = function (text1, text2) {
  // Edge case
  if (text1.length === 1 && text2.length === 1 && text1 === text2) return 1;

  let dp = Array.from({ length: text1.length + 1 }, () =>
    Array(text2.length + 1).fill(0)
  );

  for (let i = 1; i <= text1.length; i++) {
    for (let j = 1; j <= text2.length; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  return dp[text1.length][text2.length];
};

// m = text1.length | n = text2.length
// TC: O(m*n)
// SC: O(m*n)
