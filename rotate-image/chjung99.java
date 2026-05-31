class Solution {
    public void rotate(int[][] matrix) {
        int tmp;
        int n = matrix.length;
        for (int i = 0; i < n; i++){
            for (int j = i; j < n; j++){
                tmp = matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = tmp;
            }
        }
        for (int i = 0; i < n; i++){
            for (int j =0; j < (int)(n/2); j++){
                tmp = matrix[i][n-1-j];
                matrix[i][n-1-j] = matrix[i][j];
                matrix[i][j] = tmp;
            }
        }
    }
}


