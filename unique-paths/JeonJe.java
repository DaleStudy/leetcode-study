import java.util.*;

// TC: O(m * n)
// SC: O(m * n)
class Solution {
    public int uniquePaths(int m, int n) {

        int[][] arr = new int[m][n];

        int upSide;
        int leftSide;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    arr[i][j] = 1;
                    continue;
                }

                upSide = i - 1 < 0 ? 0 : arr[i - 1][j];
                leftSide = j - 1 < 0 ? 0 : arr[i][j - 1];
                arr[i][j] = upSide + leftSide;
            }
        }

        return arr[m - 1][n - 1];
    }
}
