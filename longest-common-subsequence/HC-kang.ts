/**
 * https://leetcode.com/problems/longest-common-subsequence
 * T.C. O(m * n)
 * S.C. O(n)
 */
function longestCommonSubsequence(text1: string, text2: string): number {
  const dp = Array.from({ length: text2.length + 1 }, () => 0);

  for (let i = 1; i <= text1.length; i++) {
    let prev = 0;
    for (let j = 1; j <= text2.length; j++) {
      const temp = dp[j];
      if (text1[i - 1] === text2[j - 1]) {
        dp[j] = prev + 1;
      } else {
        dp[j] = Math.max(dp[j], dp[j - 1]);
      }
      prev = temp;
    }
  }

  return dp[text2.length];
}
