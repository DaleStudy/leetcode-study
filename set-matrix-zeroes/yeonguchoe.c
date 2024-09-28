void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {

    int row_size = matrixSize;
    int column_size = matrixColSize[0];

    bool zero_on_first_row = false;
    bool zero_on_first_column = false;

    // 첫번째 row에 0이 존재하는지 확인
    for (int i = 0; i < column_size; i++) {
        if (matrix[0][i] == 0) {
            zero_on_first_row = true;
        }
    }
    // 첫번째 column에 0이 존재하는지 확인
    for (int i = 0; i < row_size; i++) {
        if (matrix[i][0] == 0) {
            zero_on_first_column = true;
        }
    }

    // 전체 돌면서 0 발견시 첫번째 row, column에 0으로 표시
    for (int i = 0; i < row_size; i++) {
        for (int j = 0; j < column_size; j++) {
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    for (int i = 1; i < row_size; i++) {
        for (int j = 1; j < column_size; j++) {
            if (matrix[0][j] == 0 || matrix[i][0] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    if (zero_on_first_row) {
        for (int i = 0; i < column_size; i++) {
            matrix[0][i] = 0;
        }
    }

    if (zero_on_first_column) {
        for (int i = 0; i < row_size; i++) {
            matrix[i][0] = 0;
        }
    }
}
// 시간 복잡도: O(matrix 크기)
// 공간 복잡도: O(1)
