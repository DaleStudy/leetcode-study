// 시간 복잡도: O(m * n)
// 공간 복잡도: O(m + n)

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
  if (!matrix || matrix.length === 0) return [];

  const rows = matrix.length;
  const cols = matrix[0].length;

  const zeroRows = new Array(rows).fill(false);
  const zeroCols = new Array(cols).fill(false);

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (matrix[row][col] === 0) {
        zeroRows[row] = true;
        zeroCols[col] = true;
      }
    }
  }

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (zeroRows[row] || zeroCols[col]) {
        matrix[row][col] = 0;
      }
    }
  }

  return matrix;
};
