var setZeroes = function (matrix) {
  let rows = new Set();
  let cols = new Set();

  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[0].length; col++) {
      if (matrix[row][col] === 0) {
        rows.add(row);
        cols.add(col);
      }
    }
  }

  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[0].length; col++) {
      if (rows.has(row) || cols.has(col)) {
        matrix[row][col] = 0;
      }
    }
  }
};

// TC: O(m*n)
// SC: O(m*n)
