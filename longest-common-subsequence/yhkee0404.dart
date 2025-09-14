class Solution {
  int longestCommonSubsequence(String text1, String text2) {
    final dp = List.generate(
                text1.length + 1,
                (_) => List.filled(text2.length + 1, 0),
            );
    for (int i = 1; i <= text1.length; i++) {
        for (int j = 1; j <= text2.length; j++) {
            dp[i][j] = text1[i - 1] == text2[j - 1] ? dp[i - 1][j - 1] + 1 : max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    return dp[text1.length][text2.length];
  }
}
