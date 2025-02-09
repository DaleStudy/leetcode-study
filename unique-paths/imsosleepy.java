// dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 점화식을 세웠는데 초기 데이터 세팅을 1로 맞추면 되는 것 때문에 진행이 안됐었음
// 결과적으로 GPT의 도움을 받음
class Solution {
    public int uniquePaths(int m, int n) {
 
        int[][] dp = new int[m][n];

        for (int i = 0; i < m; i++) dp[i][0] = 1;
        for (int j = 0; j < n; j++) dp[0][j] = 1;

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        return dp[m - 1][n - 1];
    }

}
