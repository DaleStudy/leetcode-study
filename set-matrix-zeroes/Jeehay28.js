// 🌈 In-Place Solution (Without extra space)
// The term "in-place" refers to algorithms or solutions that modify the input data directly,
// without needing extra space for a separate copy of the data. In an in-place solution,
// the operations are performed using a fixed amount of extra memory, typically O(1) space, beyond the input data itself.

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */

// Time Complexity: O(m * n)
// Space Complexity: O(1)
var setZeroes = function (matrix) {
  const rows = matrix.length;
  const cols = matrix[0].length;

  let firstRowHasZero = false;
  let firstColHasZero = false;

  // Check if the first row has any zero
  for (let c = 0; c < cols; c++) {
    if (matrix[0][c] === 0) {
      firstRowHasZero = true;
      break;
    }
  }

  // Check if the first column has any zero
  for (let r = 0; r < rows; r++) {
    if (matrix[r][0] === 0) {
      firstColHasZero = true;
      break;
    }
  }

  // Use first row and column to mark zeros
  for (let i = 1; i < rows; i++) {
    for (let j = 1; j < cols; j++) {
      if (matrix[i][j] === 0) {
        matrix[0][j] = 0;
        matrix[i][0] = 0;
      }
    }
  }

  // Set zeros based on marks in the first row and column
  for (let i = 1; i < rows; i++) {
    for (let j = 1; j < cols; j++) {
      if (matrix[0][j] === 0 || matrix[i][0] === 0) {
        matrix[i][j] = 0;
      }
    }
  }

  // Handle first row
  if (firstRowHasZero) {
    for (let c = 0; c < cols; c++) {
      matrix[0][c] = 0;
    }
  }

  // Handle first column
  if (firstColHasZero) {
    for (let r = 0; r < rows; r++) {
      matrix[r][0] = 0;
    }
  }

  return matrix;
};

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */

// 💪 My initial approach with Set...
// Time Complexity: O(m * n)
// Space Complexity: O(m + n)
var setZeroes = function (matrix) {
  let rows = new Set();
  let cols = new Set();

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      if (matrix[i][j] === 0) {
        rows.add(i);
        cols.add(j);
      }
    }
  }

  for (row of rows) {
    matrix[row] = new Array(matrix[0].length).fill(0);
  }

  for (col of cols) {
    for (let row = 0; row < matrix.length; row++) {
      matrix[row][col] = 0;
    }
  }

  return matrix;
};


