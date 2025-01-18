import java.util.HashSet;
import java.util.Set;

// 시간 복잡도: O(row x col)
// 공간 복잡도: O(row x col)
class Solution {

  public void setZeroes(int[][] matrix) {
    int row = matrix.length;
    int col = matrix[0].length;

    // 행과 열에 0이 있는지 체크할 배열
    Set<Integer> rowZero = new HashSet<>();
    Set<Integer> colZero = new HashSet<>();

    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        if (matrix[i][j] == 0) {
          rowZero.add(i);
          colZero.add(j);
        }
      }
    }

    // 행을 0으로 설정
    for (int r : rowZero) {
      for (int c = 0; c < col; c++) {
        matrix[r][c] = 0;
      }
    }

    // 열을 0으로 설정
    for (int c : colZero) {
      for (int r = 0; r < row; r++) {
        matrix[r][c] = 0;
      }
    }
  }
}

