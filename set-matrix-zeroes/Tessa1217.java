import java.util.Arrays;

/**
 * m x n 행렬 matrix가 주어질 때, 요소가 0이라면 0을 포함하는 해당 요소를 포함하는 전체 행과 열을 
 * 0으로 세팅하세요.
 */
class Solution {

    // Follow Up : 공간 복잡도 개선 필요
    // mark first row and column as marker to set 0's
    // 시간복잡도: O(m * n), 공간복잡도: O(1)
    public void setZeroes(int[][] matrix) {

        boolean firstZero = false;

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    if (j == 0) {
                        firstZero = true;
                    } else {
                        matrix[0][j] = 0;
                    }
                }
            }
        }

        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        if (matrix[0][0] == 0) {
            Arrays.fill(matrix[0], 0);
        }

        if (firstZero) {
            for (int i = 0; i < matrix.length; i++) {
                matrix[i][0] = 0;
            }
        }
    }

    // 시간복잡도: O (m * n), 공간복잡도: O(m + n)
    // public void setZeroes(int[][] matrix) {

    //     // 0을 포함하는 행과 열의 위치 저장        
    //     Set<Integer> rowsContainZeros = new HashSet<>();
    //     Set<Integer> colsContainZeros = new HashSet<>();

    //     for (int i = 0; i < matrix.length; i++) {
    //         for (int j = 0; j < matrix[0].length; j++) {
    //             if (matrix[i][j] == 0) {
    //                 rowsContainZeros.add(i);
    //                 colsContainZeros.add(j);
    //             }
    //         }
    //     }

    //     for (int row : rowsContainZeros) {
    //         for (int j = 0; j < matrix[0].length; j++) {
    //             matrix[row][j] = 0;
    //         }
    //     }        

    //     for (int col : colsContainZeros) {
    //         for (int i = 0; i < matrix.length; i++) {
    //             matrix[i][col] = 0;
    //         }
    //     }
    // }


}

