import java.util.*;
class Solution {
    /**
     * time-complexity : O(n * m)
     * space-complexity : O(1) (excluding the output List)
     */
    public List<Integer> spiralOrder(int[][] matrix) {

        List<Integer> result = new ArrayList<>();

        int left = 0;
        int right = matrix[0].length - 1;
        int top = 0;
        int bottom = matrix.length - 1;

        while (left <= right && top <= bottom) {

            // 위쪽 행을 순회한 후, 상단 경계를 1 증가
            for (int y = left; y <= right; y++) {
                result.add(matrix[top][y]);
            }
            top++;

            // 상단 인덱스가 하단 인덱스 보다 커지면 순회 중단
            if (top > bottom) break;

            // 우측 열을 순회한 후, 우측 경계를 1 감소
            for (int x = top; x <= bottom; x++) {
                result.add(matrix[x][right]);
            }
            right--;

            // 우측 인덱스가 좌측 인덱스보다 작아지면 순회 중단
            if (right < left) break;

            // 아래쪽 행을 순회한 후, 하단 경계를 1 감소
            for (int y = right; y >= left; y--) {
                result.add(matrix[bottom][y]);
            }
            bottom--;

            // 왼쪽 열을 순회한 후, 좌측 경계를 1 증가
            for (int x = bottom; x >= top; x--) {
                result.add(matrix[x][left]);
            }
            left++;

        }
        return result;

    }

}
