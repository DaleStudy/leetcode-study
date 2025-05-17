/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
   if (matrix.length === 0) return [];

    const result = [];
    const rows = matrix.length;
    const cols = matrix[0].length;

    let top = 0, bottom = rows - 1, left = 0, right = cols - 1;

    while (top <= bottom && left <= right) {
        for (let i = left; i <= right; i++) {
            result.push(matrix[top][i]);
        }
        top += 1;

        for (let i = top; i <= bottom; i++) {
            result.push(matrix[i][right]);
        }
        right -= 1;

        if (top <= bottom) {
            for (let i = right; i >= left; i--) {
                result.push(matrix[bottom][i]);
            }
            bottom -= 1;
        }

        if (left <= right) {
            for (let i = bottom; i >= top; i--) {
                result.push(matrix[i][left]);
            }
            left += 1;
        }
    }

    return result;
};
