/**
 * https://leetcode.com/problems/longest-common-subsequence/submissions/1644426037/
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function (text1, text2) {
  const m = text1.length;
  const n = text2.length;

  // Create 2D array initialized with 0
  const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

  // Fill the dp table
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        // Characters match
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        // No match, take the max from left or top cell
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }

  // The length of the longest common subsequence
  return dp[m][n];
};
