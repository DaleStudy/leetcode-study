/**
 * <a href="https://leetcode.com/problems/set-matrix-zeroes/">week7-5.set-matrix-zeroes</a>
 * <li>Description: Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's</li>
 * <li>Topics: Array, Hash Table, Matrix        </li>
 * <li>Time Complexity: O(MN), Runtime 0ms      </li>
 * <li>Space Complexity: O(M+N), Memory 45.58MB </li>
 */
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        boolean[] rowZero = new boolean[m];
        boolean[] colZero = new boolean[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    rowZero[i] = true;
                    colZero[j] = true;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            if (rowZero[i]) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = 0;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            if (colZero[i]) {
                for (int j = 0; j < m; j++) {
                    matrix[j][i] = 0;
                }
            }
        }

    }
}
