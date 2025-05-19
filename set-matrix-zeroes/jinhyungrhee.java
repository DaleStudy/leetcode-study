class Solution {

    static int MARKER = 987654321;
    public void setZeroes(int[][] matrix) {

        int width = matrix.length;
        int height = matrix[0].length;

        for (int i = 0; i < width; i++) {
            for (int j = 0; j < height; j++) {
                if(matrix[i][j] == 0) {
                    for (int x = 0; x < width; x++) {
                        if (matrix[x][j] != 0) matrix[x][j] = MARKER;
                    }
                    for (int y = 0; y < height; y++) {
                        if (matrix[i][y] != 0) matrix[i][y] = MARKER;
                    }
                }
            }
        }

        for (int i = 0; i < width; i++) {
            for (int j = 0; j < height; j++) {
                if (matrix[i][j] == MARKER) matrix[i][j] = 0;
            }
        }

    }
}
