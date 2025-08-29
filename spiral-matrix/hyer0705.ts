function spiralOrder(matrix: number[][]): number[] {
  const m = matrix.length;
  const n = matrix[0].length;

  const spiral: number[] = [];

  let top = 0;
  let bottom = m - 1;
  let left = 0;
  let right = n - 1;

  // right -> bottom -> left -> top
  while (left <= right && top <= bottom) {
    for (let i = left; i <= right; i++) {
      spiral.push(matrix[top][i]);
    }
    top++;

    for (let i = top; i <= bottom; i++) {
      spiral.push(matrix[i][right]);
    }
    right--;

    if (left <= right && top <= bottom) {
      for (let i = right; i >= left; i--) {
        spiral.push(matrix[bottom][i]);
      }
      bottom--;

      for (let i = bottom; i >= top; i--) {
        spiral.push(matrix[i][left]);
      }
      left++;
    }
  }

  return spiral;
}
