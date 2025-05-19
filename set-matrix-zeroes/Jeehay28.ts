/**
 Do not return anything, modify matrix in-place instead.
 */

// TC: O(m * n)
// ✅ SC: O(1)
function setZeroes(matrix: number[][]): void {
  let isFirstRowZero: boolean = false;
  let isFirstColZero: boolean = false;

  // check if the first row has any zeros
  for (let col = 0; col < matrix[0].length; col++) {
    if (matrix[0][col] === 0) {
      isFirstRowZero = true;
      break;
    }
  }

  // check if the first column has any zeros
  for (let row = 0; row < matrix.length; row++) {
    if (matrix[row][0] === 0) {
      isFirstColZero = true;
      break;
    }
  }

  // Use the first row and column to mark rows and columns that need to be zeroed
  for (let row = 1; row < matrix.length; row++) {
    for (let col = 1; col < matrix[0].length; col++) {
      if (matrix[row][col] === 0) {
        matrix[row][0] = 0;
        matrix[0][col] = 0;
      }
    }
  }

  // Set matrix cells to zero based on markers in the first row and column
  for (let row = 1; row < matrix.length; row++) {
    for (let col = 1; col < matrix[0].length; col++) {
      if (matrix[row][0] === 0 || matrix[0][col] === 0) {
        matrix[row][col] = 0;
      }
    }
  }

  // Zero out the first row if needed
  if (isFirstRowZero) {
    for (let col = 0; col < matrix[0].length; col++) {
      matrix[0][col] = 0;
    }
  }

  // Zero out the first column if needed
  if (isFirstColZero) {
    for (let row = 0; row < matrix.length; row++) {
      matrix[row][0] = 0;
    }
  }
}


// TC: O(m * n)
// SC: O(m + n)
/* 
function setZeroes(matrix: number[][]): void {

    const rows = new Set<number>();
    const cols = new Set<number>();

    // Identify all rows and columns that contain at least one zero
    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix[0].length; col++) {
            if (matrix[row][col] === 0) {
                rows.add(row);
                cols.add(col);
            }
        }
    }

    // Set all elements in the identified rows to zero
    for (const row of rows) {
        for (let col = 0; col < matrix[0].length; col++) {
            matrix[row][col] = 0;
        }
    }

    // Set all elements in the identified columns to zero
    for (const col of cols) {
        for (let row = 0; row < matrix.length; row++) {
            matrix[row][col] = 0;
        }
    }
};
*/

