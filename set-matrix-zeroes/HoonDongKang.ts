/**
 * [Problem]: [73] Set Matrix Zeroes
 * (https://leetcode.com/problems/set-matrix-zeroes/description/)
 */
/**
 Do not return anything, modify matrix in-place instead.
 1. 0의 모든 행과 열을 0으로 변환
 2. 변경된 0과 기존 0의 차이를 만들어야 할 것 ( #으로 바꾸고 나중에 0 변환?)
 */

function setZeroes(matrix: number[][] | string[][]): void {
    //시간복잡도 O(n^2)
    //공간복잡도 O(n)
    //통과는 하였지만 타입 조건을 변경해서 풀이
    function bruteForceFunc(matrix: number[][] | string[][]): void {
        const CHANGED_NUMBER = "#";
        const rows = matrix.length;
        const cols = matrix[0].length;

        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                if (matrix[i][j] === 0) {
                    let top = i - 1;
                    let bottom = i + 1;
                    let left = j - 1;
                    let right = j + 1;

                    while (top >= 0) {
                        if (matrix[top][j] !== 0) matrix[top][j] = CHANGED_NUMBER;
                        top--;
                    }
                    while (bottom < rows) {
                        if (matrix[bottom][j] !== 0) matrix[bottom][j] = CHANGED_NUMBER;
                        bottom++;
                    }
                    while (left >= 0) {
                        if (matrix[i][left] !== 0) matrix[i][left] = CHANGED_NUMBER;
                        left--;
                    }
                    while (right < cols) {
                        if (matrix[i][right] !== 0) matrix[i][right] = CHANGED_NUMBER;
                        right++;
                    }
                }
            }
        }

        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                if (matrix[i][j] === CHANGED_NUMBER) matrix[i][j] = 0;
            }
        }
    }

    //시간복잡도 O(m * n)
    //공간복잡도 O(m + n)
    function setFunc(matrix: number[][]): void {
        const rows = matrix.length;
        const cols = matrix[0].length;
        let zeroRows = new Set<number>();
        let zeroCols = new Set<number>();

        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                if (matrix[i][j] === 0) {
                    zeroCols.add(j);
                    zeroRows.add(i);
                }
            }
        }

        for (let r of zeroRows) {
            for (let i = 0; i < cols; i++) {
                matrix[r][i] = 0;
            }
        }

        for (let c of zeroCols) {
            for (let i = 0; i < rows; i++) {
                matrix[i][c] = 0;
            }
        }
    }

    //시간복잡도 O(m * n)
    //공간복잡도 O(1)
    function optimizeSpaceFunc(matrix: number[][]): void {
        const rows = matrix.length;
        const cols = matrix[0].length;
        let isFirstRowZero = false;
        let isFirstColZero = false;

        for (let i = 0; i < rows; i++) {
            if (matrix[i][0] === 0) isFirstColZero = true;
        }

        for (let j = 0; j < cols; j++) {
            if (matrix[0][j] === 0) isFirstRowZero = true;
        }

        for (let i = 1; i < rows; i++) {
            for (let j = 1; j < cols; j++) {
                if (matrix[i][j] === 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }

        for (let i = 1; i < rows; i++) {
            for (let j = 1; j < cols; j++) {
                if (matrix[i][0] === 0 || matrix[0][j] === 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        if (isFirstColZero) {
            for (let i = 0; i < rows; i++) {
                matrix[i][0] = 0;
            }
        }

        if (isFirstRowZero) {
            for (let j = 0; j < cols; j++) {
                matrix[0][j] = 0;
            }
        }
    }
}
