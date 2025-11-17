class Solution {
    // dp 표를 봐야 이해가 더 쉽다. https://twinw.tistory.com/126
    // dp, 즉 메모이제이션의 범위는 이전 row인 것이다. (기존 cell 위주의 문제보다 넓은 범위)
    public int longestCommonSubsequence(String text1, String text2) {
        // 왼쪽과 위로 1줄씩 버퍼(여유) 배열이 있다. 즉, dp[0][..], dp[..][0]은 0으로 초기화된 상태
        int m = text1.length();
        int n = text2.length();

        int[][] dp = new int[m+1][n+1];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // DP 계산을 +1로 했어야 했는데 이전 케이스를 재사용하는 -1로만 접근해서 범위 에러가 많이 났었다.
                if (text1.charAt(i) == text2.charAt(j)) {
                    dp[i + 1][j + 1] = dp[i][j] + 1;
                } else {
                    dp[i + 1][j + 1] = Math.max(dp[i][j + 1], dp[i + 1][j]);
                }
            }
        }

        return dp[m][n];
    }

    // -1을 참조해 이전 케이스를 재사용하는 경우는 1부터 m,n까지 하면 그렇게 할 수 있다.
    public int longestCommonSubsequence2(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;  // 문자가 같으면 대각선 값 + 1
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);  // 위 or 왼쪽 중 큰 값
                }
            }
        }

        return dp[m][n];
    }
}
