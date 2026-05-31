class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        /**
        1.문제: 가장 긴 common subsequence length return, 없으면 0 return
        2.constraints
        - length min = 1, max = 1000
        - text1, text2 모두 lowercase로 구성
        3.풀이
        - dp[i][j] = text1의 앞 i개, text2의 앞 j개를 비교했을 때 LCS 길이
        - 문자가 같으면: dp[i][j] = dp[i-1][j-1] + 1
        - 문자가 다르면: dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
         */
        int t1Size = text1.length(); //row
        int t2Size = text2.length(); //col
        int[][] dp = new int[t1Size + 1][t2Size + 1];

        for(int i = 1; i <= t1Size; i++) {
            for(int j = 1; j <= t2Size; j++) {
                if(text1.charAt(i-1) == text2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[t1Size][t2Size];
    }
}
