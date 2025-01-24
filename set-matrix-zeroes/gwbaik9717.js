// m: height of matrix, n: width of matrix
// Time complexity: O(m*n)
// Space complexity: O(m+n)

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
  const h = matrix.length;
  const w = matrix[0].length;

  const setY = new Set();
  const setX = new Set();

  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (matrix[i][j] === 0) {
        setY.add(i);
        setX.add(j);
      }
    }
  }

  for (const y of setY) {
    for (let x = 0; x < w; x++) {
      matrix[y][x] = 0;
    }
  }

  for (const x of setX) {
    for (let y = 0; y < h; y++) {
      matrix[y][x] = 0;
    }
  }
};
