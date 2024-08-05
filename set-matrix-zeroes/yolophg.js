// Time Complexity: O(rows * cols)
// Space Complexity: O(1)

var setZeroes = function (matrix) {
  // number of rows in the matrix
  const rows = matrix.length;
  // number of cols in the matrix
  const cols = matrix[0].length;
  // to check if the first row has any zeros
  let rowZero = false;
  // to check if the first col has any zeros
  let colZero = false;

  // check if the first row has any zeros
  for (let c = 0; c < cols; c++) {
    if (matrix[0][c] === 0) {
      rowZero = true;
      break;
    }
  }

  // check if the first col has any zeros
  for (let r = 0; r < rows; r++) {
    if (matrix[r][0] === 0) {
      colZero = true;
      break;
    }
  }

  // use the first row and col to mark zeros
  for (let r = 1; r < rows; r++) {
    for (let c = 1; c < cols; c++) {
      if (matrix[r][c] === 0) {
        // mark corresponding col in first row
        matrix[0][c] = 0;
        // mark corresponding row in first col
        matrix[r][0] = 0;
      }
    }
  }

  // set matrix elements to zero based on markers in the first row and col
  for (let r = 1; r < rows; r++) {
    for (let c = 1; c < cols; c++) {
      if (matrix[0][c] === 0 || matrix[r][0] === 0) {
        matrix[r][c] = 0;
      }
    }
  }

  // handle the first row if there was any zero
  if (rowZero) {
    for (let c = 0; c < cols; c++) {
      matrix[0][c] = 0;
    }
  }

  // handle the first col if there was any zero
  if (colZero) {
    for (let r = 0; r < rows; r++) {
      matrix[r][0] = 0;
    }
  }
};
