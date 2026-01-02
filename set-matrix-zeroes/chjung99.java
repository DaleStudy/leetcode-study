class Solution {
    int m;
    int n;
    public void setZeroes(int[][] matrix) {
        m = matrix.length;
        n = matrix[0].length;

        Set<Integer> rows = new HashSet<>();
        Set<Integer> cols = new HashSet<>();

        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (matrix[i][j] == 0){
                    rows.add(i);
                    cols.add(j);
                }
            }
        }

        for (int row : rows) {
            setZeroRow(row, matrix);
        }

        for (int col : cols) {
            setZeroCol(col, matrix);
        }
    }

    public void setZeroCol(int col, int[][] matrix){
        for (int i = 0; i < m; i++) {
            matrix[i][col] = 0;
        }
    }

    public void setZeroRow(int row, int[][] matrix){
        for (int i = 0; i < n; i++) {
            matrix[row][i] = 0;
        }
    }
}


