/**
 * <a href="https://leetcode.com/problems/longest-common-subsequence/">week8-4.longest-common-subsequence</a>
 * <li>Description: Given two strings text1 and text2, return the length of their longest common subsequence</li>
 * <li>Topics: String, Dynamic Programming</li>
 * <li>Time Complexity: O(M×N), Runtime 11ms</li>
 * <li>Space Complexity: O(M×N), Memory 50.97MB</li>
 */

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            char c1 = text1.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                char c2 = text2.charAt(j - 1);

                if (c1 == c2) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[m][n];
    }
}
