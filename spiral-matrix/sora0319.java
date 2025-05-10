import java.util.*;

class SolutionSpiral {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();

        if (matrix == null || matrix.length == 0) return result;

        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            // Traverse from left to right
            for (int col = left; col <= right; col++) {
                result.add(matrix[top][col]);
            }
            top++;

            if (top > bottom) break;

            for (int row = top; row <= bottom; row++) {
                result.add(matrix[row][right]);
            }
            right--;

            if (left > right) break;

            for (int col = right; col >= left; col--) {
                result.add(matrix[bottom][col]);
            }
            bottom--;

            for (int row = bottom; row >= top; row--) {
                result.add(matrix[row][left]);
            }
            left++;
        }

        return result;
    }
}

