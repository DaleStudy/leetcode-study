/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    
    let firstRowHasZero = false;
    let firstColHasZero = false;

    // 첫 행/열에 0이 있는지 확인
    for (let i = 0; i < m; i++) {
        if (matrix[i][0] === 0) firstColHasZero = true;
    }
    for (let j = 0; j < n; j++) {
        if (matrix[0][j] === 0) firstRowHasZero = true;
    }

    // 마커로 0 표시
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (matrix[i][j] === 0) {
                matrix[i][0] = 0; // 해당 행 마킹
                matrix[0][j] = 0; // 해당 열 마킹
            }
        }
    }

    // 마커 기반으로 행/열 0 처리
    for (let i = 1; i < m; i++) {
        if (matrix[i][0] === 0) {
            for (let j = 1; j < n; j++) {
                matrix[i][j] = 0;
            }
        }
    }
    for (let j = 1; j < n; j++) {
        if (matrix[0][j] === 0) {
            for (let i = 1; i < m; i++) {
                matrix[i][j] = 0;
            }
        }
    }

    // Step 4: 첫 행과 첫 열 처리
    if (firstRowHasZero) {
        for (let j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }
    if (firstColHasZero) {
        for (let i = 0; i < m; i++) {
            matrix[i][0] = 0;
        }
    }
};
