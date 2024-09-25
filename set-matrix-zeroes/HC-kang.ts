/**
 * https://leetcode.com/problems/set-matrix-zeroes
 * T.C. O(r * c)
 * S.C. O(r + c)
 */
function setZeroes(matrix: number[][]): void {
  const r = matrix.length;
  const c = matrix[0].length;

  const zeroRows = new Set<number>();
  const zeroCols = new Set<number>();

  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      if (matrix[i][j] === 0) {
        zeroRows.add(i);
        zeroCols.add(j);
      }
    }
  }

  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      if (zeroRows.has(i) || zeroCols.has(j)) {
        matrix[i][j] = 0;
      }
    }
  }
}

/**
 * T.C. O(r * c)
 * S.C. O(1)
 */
function setZeroes(matrix: number[][]): void {
  const r = matrix.length;
  const c = matrix[0].length;

  let firstRowHasZero = false;
  let firstColHasZero = false;

  if (matrix[0].some((val) => val === 0)) {
    firstRowHasZero = true;
  }

  if (matrix.some((row) => row[0] === 0)) {
    firstColHasZero = true;
  }

  for (let i = 1; i < r; i++) {
    for (let j = 1; j < c; j++) {
      if (matrix[i][j] === 0) {
        matrix[i][0] = 0;
        matrix[0][j] = 0;
      }
    }
  }

  for (let i = 1; i < r; i++) {
    if (matrix[i][0] === 0) {
      matrix[i].fill(0);
    }
  }

  for (let j = 1; j < c; j++) {
    if (matrix[0][j] === 0) {
      matrix.forEach((row) => (row[j] = 0));
    }
  }

  if (firstRowHasZero) {
    matrix[0].fill(0);
  }

  if (firstColHasZero) {
    matrix.forEach((row) => (row[0] = 0));
  }
}
