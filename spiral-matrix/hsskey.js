/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    if (matrix.length === 0) return [];

    const res = [];
    let left = 0, right = matrix[0].length;
    let top = 0, bottom = matrix.length;

    while (left < right && top < bottom) {
        // 상단 행 왼쪽 → 오른쪽
        for (let i = left; i < right; i++) {
            res.push(matrix[top][i]);
        }
        top += 1;

        // 오른쪽 열 위 → 아래
        for (let i = top; i < bottom; i++) {
            res.push(matrix[i][right - 1]);
        }
        right -= 1;

        if (!(left < right && top < bottom)) break;

        // 하단 행 오른쪽 → 왼쪽
        for (let i = right - 1; i >= left; i--) {
            res.push(matrix[bottom - 1][i]);
        }
        bottom -= 1;

        // 왼쪽 열 아래 → 위
        for (let i = bottom - 1; i >= top; i--) {
            res.push(matrix[i][left]);
        }
        left += 1;
    }

    return res;
};
