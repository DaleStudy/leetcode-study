/*
   [Approch 1]
   - time: O(m*n)
   - space: O(m*n)
 */
class Solution {

    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];

        for (int[] row : dp) {
            Arrays.fill(row, 1);
        }

        for (int row = 1; row < m; row++) {
            for (int col = 1; col < n; col++) {
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1];
            }
        }

        return dp[m - 1][n - 1];
    }
}

/*
   [Approch 2]
   - time: O(m*n)
   - space: O(n)
 */
class Solution {

    public int uniquePaths(int m, int n) {
        int[] upper = new int[n];

        Arrays.fill(upper, 1);

        for (int i = 1; i < m; i++) {
            int left = 1;
            for (int j = 1; j < n; j++) {
                left += upper[j];
                upper[j] = left;
            }
        }

        return upper[n - 1];
    }
}
