var rotate = function (matrix) {
  let top = 0,
    bottom = matrix.length - 1;
  let left, right;

  while (top < bottom) {
    (left = top), (right = bottom);

    for (let i = 0; i < bottom - top; i++) {
      const topLeft = matrix[top][left + i];
      matrix[top][left + i] = matrix[bottom - i][left];
      matrix[bottom - i][left] = matrix[bottom][right - i];
      matrix[bottom][right - i] = matrix[top + i][right];
      matrix[top + i][right] = topLeft;
    }

    top++;
    bottom--;
  }
};

// TC: O(n^2)
// SC: O(1)
