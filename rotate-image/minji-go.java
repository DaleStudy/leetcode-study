/**
 * <a href="https://leetcode.com/problems/rotate-image/">week15-4. rotate-image</a>
 * <li>Description: Given an n x n 2D matrix representing an image, rotate the image by 90 degrees</li>
 * <li>Topics: Array, Math, Matrix</li>
 * <li>Time Complexity: O(N²), Runtime 0ms      </li>
 * <li>Space Complexity: O(1), Memory 42.11MB   </li>
 */

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;

        for (int i = 0; i < n / 2; i++) {
            for (int j = i; j < n - 1 - i; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - j][i];
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j];
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i];
                matrix[j][n - 1 - i] = temp;
            }
        }
    }
}

