// Time complexity: O(n^2)
// Space complexity: O(1)

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
  let top = 0;
  let bottom = matrix.length - 1;

  while (top < bottom) {
    for (let i = 0; i < bottom - top; i++) {
      const left = top;
      const right = bottom;

      const temp = matrix[top][left + i];

      matrix[top][left + i] = matrix[bottom - i][left];
      matrix[bottom - i][left] = matrix[bottom][right - i];
      matrix[bottom][right - i] = matrix[top + i][right];
      matrix[top + i][right] = temp;
    }

    top++;
    bottom--;
  }
};
