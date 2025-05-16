/**
 * m x n 행렬이 있을 때 로봇이 상단-좌측 가장자리에서 하단-우측 가장자리로 갈 수 있는 경우의 수 구하기
 * 로봇은 오른쪽 또는 밑으로만 움직일 수 있음
 */
class Solution {

    // DFS 시간 초과로 DP로 구현
    // 시간복잡도: O(m * n)
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];

        // 첫째 열
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }

        // 첫째 행
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]; // 위, 왼쪽 값
            }
        }

        return dp[m - 1][n - 1];

    }

    // DFS 시간 초과
    // private int cnt = 0;
    // int[] dx = {1, 0};
    // int[] dy = {0, 1};    

    // public int uniquePaths(int m, int n) {
    //     int[][] path = new int[m][n];
    //     dfs(0, 0, path);
    //     return cnt;
    // }

    // private void dfs(int x, int y, int[][] path) {

    //     if (x == path.length - 1 && y == path[0].length - 1) {
    //         cnt++;
    //         return;            
    //     }

    //     path[x][y] = 1;

    //     for (int i = 0; i < 2; i++) {
    //         int nx = x + dx[i];
    //         int ny = y + dy[i];
    //         if (nx >= 0 && nx < path.length && ny >= 0 && ny < path[0].length && path[nx][ny] != 1) {
    //             dfs(nx, ny, path);
    //         }            
    //     }

    //     path[x][y] = 0;

    // }
}

