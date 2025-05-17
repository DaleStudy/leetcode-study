class Solution {
    public void setZeroes(int[][] matrix) {
        int M = matrix.length;
        int N = matrix[0].length;

        boolean firstRow = false;
        boolean firstCol = false;

        for(int i = 0; i < M; i++){
            if(matrix[i][0] == 0){
                firstRow = true;
                break;
            }
        }

        for(int j = 0; j < N; j++){
            if(matrix[0][j] == 0){
                firstCol = true;
                break;
            }
        }

        for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for(int i = 1; i < M; i++){
            for(int j = 1; j < N; j++){
                if(matrix[i][0] == 0 || matrix[0][j] == 0) matrix[i][j] = 0;
            }
        }

        if(firstRow){
            for(int i = 0; i < M; i++){
                matrix[i][0] = 0;
            }
        }

        if(firstCol){
            for(int j = 0; j < N; j++){
                matrix[0][j] = 0;
            }
        }
    }
}

