class Solution {
    public int uniquePaths(int m, int n) {
        /**
         * 여기서 이동가능한 경우는 right, down 두가지 경우이다.
         * 모든 블록은 내 왼쪽 블록에서 나로 온 경우, 내 위 블록에서 나로 온 경우를 고려해서 [i-1][j] + [i][j-1]로 표현할 수 있다.
         * 단 가로 첫번째 줄과 세로 첫번째 줄은 1로 초기화 해줘야 한다. (왜냐하면 각각 down, right이 없기 때문에 그 블록들은 1가지 경우로밖에 도달할 수 없기 때문이다.)
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
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m - 1][n - 1];
    }
}
