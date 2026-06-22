class Solution {
    public int uniquePaths(int m, int n) {
        /**
        1.문제: finish로 가는 unique path 수
        2.constraints:
        - m: 세로, n = 가로
        - m,n min = 1, max = 100
        - right, down 으로만 움직이기 가능
        3.solution
        - dfs ?? => x, 모든 경로 탐색하지 않음
        - dp => [i][j] = [i-1][j] + [i][j-1]
        - time: O(mn), space: O(n)
         */

         int[][] dp = new int[m][n];

        //첫행, 첫열 = 1
         for(int i =0; i<m; i++) {
            dp[i][0] = 1;
         }

         for(int i = 0; i < n; i++) {
            dp[0][i] = 1;
         }

         for(int i = 1; i< m; i++) {
            for(int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
         }
        return dp[m-1][n-1];
    }
}
