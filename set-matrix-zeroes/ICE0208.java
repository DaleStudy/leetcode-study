import java.util.Arrays;

class Solution {
    public void setZeroes(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        // 첫 번째 행과 열은 marker로 사용하므로, 원래 0이 있었는지 별도로 저장한다.
        boolean firstRowHasZero = false;
        for (int col = 0; col < cols; ++col) {
            if (matrix[0][col] == 0) {
                firstRowHasZero = true;
                break;
            }
        }

        boolean firstColumnHasZero = false;
        for (int row = 0; row < rows; ++row) {
            if (matrix[row][0] == 0) {
                firstColumnHasZero = true;
                break;
            }
        }

        // 첫 번째 행과 열을 각 행과 열의 zero marker로 사용한다.
        for (int row = 1; row < rows; ++row) {
            for (int col = 1; col < cols; ++col) {
                if (matrix[row][col] == 0) {
                    matrix[row][0] = 0;
                    matrix[0][col] = 0;
                }
            }
        }

        // marker를 기준으로 내부 원소를 0으로 변경한다.
        for (int row = 1; row < rows; ++row) {
            for (int col = 1; col < cols; ++col) {
                if (matrix[row][0] == 0 || matrix[0][col] == 0) {
                    matrix[row][col] = 0;
                }
            }
        }

        if (firstRowHasZero) {
            Arrays.fill(matrix[0], 0);
        }

        if (firstColumnHasZero) {
            for (int row = 0; row < rows; ++row) {
                matrix[row][0] = 0;
            }
        }
    }
}
