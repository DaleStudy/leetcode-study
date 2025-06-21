/**
 * 두 문자열 text1과 text2가 주어질 때 가장 긴 공통 부분 수열의 길이를 리턴하고 없으면 0을 리턴하세요.
 */
class Solution {

    // 시간복잡도: O(t1Length * t2Length)
    public int longestCommonSubsequence(String text1, String text2) {

        int t1Length = text1.length();
        int t2Length = text2.length();

        int[][]dp = new int[t1Length + 1][t2Length + 1];

        for (int i = 1; i <= t1Length; i++) {
            for (int j = 1; j <= t2Length; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[t1Length][t2Length];

    }
}

