var spiralOrder = function (matrix) {
  // Edge case
  if (matrix.length === 0) return [];

  let result = [];
  let rowStart = 0,
    rowEnd = matrix.length - 1;
  let colStart = 0,
    colEnd = matrix[0].length - 1;

  while (rowStart <= rowEnd && colStart <= colEnd) {
    // Traverse right
    for (let col = colStart; col <= colEnd; col++) {
      result.push(matrix[rowStart][col]);
    }
    rowStart++;

    // Traverse down
    for (let row = rowStart; row <= rowEnd; row++) {
      result.push(matrix[row][colEnd]);
    }
    colEnd--;

    // Traverse left (check if rowStart <= rowEnd to avoid duplicates)
    if (rowStart <= rowEnd) {
      for (let col = colEnd; col >= colStart; col--) {
        result.push(matrix[rowEnd][col]);
      }
      rowEnd--;
    }

    // Traverse up (check if colStart <= colEnd to avoid duplicates)
    if (colStart <= colEnd) {
      for (let row = rowEnd; row >= rowStart; row--) {
        result.push(matrix[row][colStart]);
      }
      colStart++;
    }
  }

  return result;
};

// TC: O(m*n)
// SC: O(m*n)
