import java.util.ArrayList;
import java.util.List;

/**
 * m * n 행렬을 시계 방향 순대로 요소를 정렬하여 반환하세요.
 */
class Solution {

    public List<Integer> spiralOrder(int[][] matrix) {

        List<Integer> spirals = new ArrayList<>();

        int top = 0;
        int bottom = matrix.length - 1;
        int start = 0;
        int end = matrix[0].length - 1;

        while (top <= bottom && start <= end) {
            // 우측
            for (int i = start; i <= end; i++) {
                spirals.add(matrix[top][i]);
            }
            top++;

            // 아래
            for (int i = top; i <= bottom; i++) {
                spirals.add(matrix[i][end]);
            }
            end--;

            // 좌측
            if (top <= bottom) {
                for (int i = end; i >= start; i--) {
                    spirals.add(matrix[bottom][i]);
                }
                bottom--;
            }

            // 위
            if (start <= end) {
                for (int i = bottom; i >= top; i--) {
                    spirals.add(matrix[i][start]);
                }
                start++;
            }

        }

        return spirals;
    }

}

