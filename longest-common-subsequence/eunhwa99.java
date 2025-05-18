class Solution {
  public int longestCommonSubsequence(String text1, String text2) {
    int n = text1.length();
    int m = text2.length();

    int[][] dp = new int[n + 1][m + 1];

    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
          dp[i][j] = dp[i - 1][j - 1] + 1;
        } else {
          dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
        }
      }
    }

    return dp[n][m];
  }
}
// Time Complexity: O(n * m)
// Space Complexity: O(n * m)
