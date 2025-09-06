// Time Complexity: O(m*n), m: number of row, n: number of column
// Space Complexity: O(m*n), m: number of row, n: number of column
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] pathMap = new int[m][n];

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 || j == 0) {
                    pathMap[i][j] = 1;
                } else {
                    pathMap[i][j] = pathMap[i-1][j] + pathMap[i][j-1];
                }
            }
        }

        return pathMap[m-1][n-1];
    }
}
