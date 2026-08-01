import java.util.*;

// TC: O(m * n)
// SC: O(1) (반환 리스트 제외)
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int n = matrix.length, m = matrix[0].length;

        // 아직 훑지 않은 직사각형의 네 벽. 한 구간을 끝낼 때마다 안쪽으로 한 칸 민다.
        int left = 0, right = m - 1, top = 0, bottom = n - 1;

        while (left <= right && top <= bottom) {
            // left to right
            for (int j = left; j <= right; j++) {
                result.add(matrix[top][j]);
            }
            top++;

            // top to bottom
            for (int i = top; i <= bottom; i++) {
                result.add(matrix[i][right]);
            }
            right--;

            // 한 줄짜리에서 이미 읽은 행·열을 되짚지 않도록 차단.
            // 왼쪽으로 못 가면 위로도 못 가므로 두 구간을 함께 건너뛴다.
            if (left > right || top > bottom) {
                break;
            }

            // right to left
            for (int j = right; j >= left; j--) {
                result.add(matrix[bottom][j]);
            }
            bottom--;

            // bottom to top
            for (int i = bottom; i >= top; i--) {
                result.add(matrix[i][left]);
            }
            left++;
        }

        return result;
    }
}
