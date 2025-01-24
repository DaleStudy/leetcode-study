// m: height of matrix, n: width of matrix
// Time complexity: O(m*n)
// Space complexity: O(1)

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
  const h = matrix.length;
  const w = matrix[0].length;

  // a flag for iterating rows of the first column
  let temp1 = false;

  // a flag for iterating cols of the first row
  let temp2 = false;

  for (let i = 0; i < h; i++) {
    if (matrix[i][0] === 0) {
      temp1 = true;
      break;
    }
  }

  for (let i = 0; i < w; i++) {
    if (matrix[0][i] === 0) {
      temp2 = true;
      break;
    }
  }

  for (let i = 1; i < h; i++) {
    for (let j = 1; j < w; j++) {
      if (matrix[i][j] === 0) {
        matrix[i][0] = 0;
        matrix[0][j] = 0;
      }
    }
  }

  for (let i = 1; i < h; i++) {
    if (matrix[i][0] === 0) {
      for (let j = 1; j < w; j++) {
        matrix[i][j] = 0;
      }
    }
  }

  for (let i = 1; i < w; i++) {
    if (matrix[0][i] === 0) {
      for (let j = 1; j < h; j++) {
        matrix[j][i] = 0;
      }
    }
  }

  if (temp1) {
    for (let i = 0; i < h; i++) {
      matrix[i][0] = 0;
    }
  }

  if (temp2) {
    for (let j = 0; j < w; j++) {
      matrix[0][j] = 0;
    }
  }
};
