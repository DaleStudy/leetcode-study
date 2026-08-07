import java.util.Arrays;

class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        // 첫 번째 행과 열은 한 방향으로만 이동해 도달할 수 있으므로 1로 초기화합니다.
        initializeBaseCases(dp);

        for (int row = 1; row < m; ++row) {
            for (int col = 1; col < n; ++col) {
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1];
            }
        }

        return dp[m - 1][n - 1];
    }

    /**
        * DP 배열의 첫 번째 행과 첫 번째 열을 1로 초기화합니다.
        * @param dp 초기화할 DP 배열
        */
    private static void initializeBaseCases(int[][] dp) {
        int rows = dp.length;
        int cols = dp[0].length;

        for (int row = 0; row < rows; row++) {
            dp[row][0] = 1;
        }
        for (int col = 0; col < cols; col++) {
            dp[0][col] = 1;
        }
    }
}

class Solution2 {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);

        for (int row = 1; row < m; ++row) {
            for (int col = 1; col < n; ++col) {
                dp[col] += dp[col - 1];
            }
        }

        return dp[n - 1];
    }
}
