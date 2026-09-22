// TC: O(m * n)
// SC: O(m * n)
class Solution {

    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp = new int[text1.length() + 1][text2.length() + 1];

        for (int i = text1.length() - 1; i >= 0; i--) {
            for (int j = text2.length() - 1; j >= 0; j--) {

                dp[i][j] = text1.charAt(i) == text2.charAt(j) ?
                        1 + dp[i + 1][j + 1] :
                        Math.max(dp[i + 1][j], dp[i][j + 1]);

            }
        }
        return dp[0][0];
    }

}
