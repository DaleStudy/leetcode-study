const setZeroes = (matrix) => {
    const ROWS = matrix.length;
    const COLS = matrix[0].length;
    let rowZero = false;

    // 1. 어떤 행과 열이 0이 되어야 하는지 기록
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            if (matrix[r][c] === 0) {
                matrix[0][c] = 0;
                if (r > 0) {
                    matrix[r][0] = 0;
                } else {
                    rowZero = true;
                }
            }
        }
    }

    // 2. 첫 번째 행과 첫 번째 열을 제외한 나머지 처리
    for (let r = 1; r < ROWS; r++) {
        for (let c = 1; c < COLS; c++) {
            if (matrix[0][c] === 0 || matrix[r][0] === 0) {
                matrix[r][c] = 0;
            }
        }
    }

    // 3. 첫 번째 열 처리
    if (matrix[0][0] === 0) {
        for (let r = 0; r < ROWS; r++) {
            matrix[r][0] = 0;
        }
    }

    // 4. 첫 번째 행 처리
    if (rowZero) {
        for (let c = 0; c < COLS; c++) {
            matrix[0][c] = 0;
        }
    }
};
