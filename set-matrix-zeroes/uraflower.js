/**
 * 주어진 격자에서 원소가 0인 행과 열의 값을 0으로 수정하는 함수
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
const setZeroes = function (matrix) {
    const m = matrix.length;
    const n = matrix[0].length;
    const rows = new Set();
    const cols = new Set();

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (matrix[r][c] === 0) {
                rows.add(r);
                cols.add(c);
            }
        }
    }

    rows.forEach((row) => matrix[row] = Array(n).fill(0));
    cols.forEach((col) => {
        for (let r = 0; r < m; r++) {
            matrix[r][col] = 0;
        }
    });
};

// 시간복잡도: O(m * n)
// 공간복잡도: O(m + n)
