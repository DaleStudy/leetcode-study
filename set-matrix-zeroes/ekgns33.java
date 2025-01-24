/**

 sol1 ) brute force
 save zero points, replace row

 read O(mn)
 save zero points
 replace row,cols
 tc : O(mn)
 sc : O(mn)

 sol2) use bitwise
 length of matrix < integer range
 use bit wise
 tc : O(mn)
 sc : O(m + n)

 sol3) use first row, col as memo
 read matrix, check to row or col if zero

 replace if row, col is marked as zero
 tc : O(mn)
 sc : O(1) in-place
 */
class Solution {
  public void setZeroes(int[][] matrix) {
    int m = matrix.length;
    int n = matrix[0].length;
    boolean firstRowZero = false;
    boolean firstColZero = false;
    for(int i = 0; i < m; i++) {
      for(int j = 0; j < n; j++) {
        if(matrix[i][j] == 0) {
          if(i == 0) firstRowZero = true;
          if(j == 0) firstColZero = true;
          matrix[i][0] = 0;
          matrix[0][j] = 0;
        }
      }
    }
    for(int i = 1; i <m; i++) {
      for(int j = 1; j < n; j++) {
        if(matrix[i][0] == 0 || matrix[0][j] == 0) {
          matrix[i][j] = 0;
        }
      }
    }
    if(firstRowZero) {
      Arrays.fill(matrix[0], 0);
    }
    if(firstColZero) {
      for(int j = 0; j <m; j++) {
        matrix[j][0] = 0;
      }
    }


  }
}
