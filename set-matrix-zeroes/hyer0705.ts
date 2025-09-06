// mark first row, first col - 0ms
/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
  const m = matrix.length;
  const n = matrix[0].length;

  let isFirstColZero = false;
  let isFirstRowZero = false;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (matrix[i][j] === 0) {
        if (!isFirstRowZero && i === 0) isFirstRowZero = true;
        if (!isFirstColZero && j === 0) isFirstColZero = true;
        matrix[i][0] = 0;
        matrix[0][j] = 0;
      }
    }
  }

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (matrix[i][0] === 0 || matrix[0][j] === 0) {
        matrix[i][j] = 0;
      }
    }
  }

  if (isFirstRowZero) {
    for (let j = 0; j < n; j++) {
      matrix[0][j] = 0;
    }
  }
  if (isFirstColZero) {
    for (let i = 0; i < m; i++) {
      matrix[i][0] = 0;
    }
  }
}

// using set - 4ms
/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
  const m = matrix.length;
  const n = matrix[0].length;

  // `${row},${col}`
  const coordinates = new Set<string>();

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (matrix[i][j] === 0) {
        coordinates.add(`${i},${j}`);
      }
    }
  }

  for (const coordinate of coordinates) {
    const [x, y] = coordinate.split(",");
    for (let j = 0; j < n; j++) {
      matrix[x][j] = 0;
    }
    for (let i = 0; i < m; i++) {
      matrix[i][y] = 0;
    }
  }
}
