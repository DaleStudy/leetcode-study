class Solution {
    int count;
    public int uniquePaths(int m, int n) {
        /**
         1. dfs + backtrack => Time Limit Exceeded
         */
        //boolean[][] visited = new boolean[m][n];
        //dfs(visited, 0, 0, m, n);

        /**
         2. DP
         - 저장되는 값은 해당 위치까지 도달할 수 있는 '고유한 경로의 수'
         */
        int[][] dp = new int[m][n];

        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // 이전에 왔던 값들을 더함(위, 왼쪽)
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        return dp[m-1][n-1];
    }

    /**
     1. DFS + backtrack
     */
    /**
     public void dfs(boolean[][] visited, int x, int y, int m, int n) {

     if (x == m - 1 && y == n - 1) {
     count++;
     return;
     }


     visited[x][y] = true;

     // 오른쪽으로 이동 + backtrack
     if (y + 1 < n && !visited[x][y + 1]) {
     dfs(visited, x, y + 1, m , n);
     }

     // 아래쪽으로 이동 + backtrack
     if (x + 1 < m && !visited[x + 1][y]) {
     dfs(visited, x + 1, y, m, n);
     }

     visited[x][y] = false;
     }
     */
}
