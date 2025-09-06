// Time Complexity: O(m*n)
// Space Complexity: O(m+n)
class Solution {
    public void setZeroes(int[][] matrix) {
        ArrayList<Integer> rowList = new ArrayList<>();
        ArrayList<Integer> colList = new ArrayList<>();

        for (int m = 0; m < matrix.length; ++m) {
            for (int n = 0; n < matrix[0].length; ++n) {
                if (matrix[m][n] != 0) continue;
                if (!rowList.contains(m)) rowList.add(m);
                if (!colList.contains(n)) colList.add(n);
            }
        }

        for (Integer row : rowList) {
            for (int n = 0;  n < matrix[0].length; ++n) {
                matrix[row][n] = 0;
            }
        }

        for (Integer col : colList) {
            for (int n = 0;  n < matrix.length; ++n) {
                matrix[n][col] = 0;
            }
        }
    }
}
