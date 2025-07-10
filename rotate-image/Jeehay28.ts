/**
 Do not return anything, modify matrix in-place instead.
 */

// TC: O(n^2)
// SC: O(1)
function rotate(matrix: number[][]): void {
  let top = 0;
  let bottom = matrix.length - 1;

  while (top < bottom) {
    let left = top;
    let right = bottom;

    for (let i = 0; i < bottom - top; i++) {
      const temp = matrix[top][left + i]; // topLeft
      matrix[top][left + i] = matrix[bottom - i][left];
      matrix[bottom - i][left] = matrix[bottom][right - i];
      matrix[bottom][right - i] = matrix[top + i][right];
      matrix[top + i][right] = temp;
    }

    top++; // top down
    bottom--; // bottom up
  }
}
