/**
 * https://leetcode.com/problems/spiral-matrix/
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  const result = [];
  if (matrix.length === 0) return result;

  let top = 0;
  let bottom = matrix.length - 1;
  let left = 0;
  let right = matrix[0].length - 1;

  while (top <= bottom && left <= right) {
    // 1. 좌 -> 우
    for (let col = left; col <= right; col++) {
      result.push(matrix[top][col]);
    }
    top++; // 위쪽 경계 한 줄 아래로 이동

    // 2. 위 -> 아래
    for (let row = top; row <= bottom; row++) {
      result.push(matrix[row][right]);
    }
    right--; // 오른쪽 경계 왼쪽으로 이동

    // 3. 우 -> 좌
    if (top <= bottom) {
      for (let col = right; col >= left; col--) {
        result.push(matrix[bottom][col]);
      }
      bottom--; // 아래쪽 경계 위로 이동
    }

    // 4. 아래 -> 위
    if (left <= right) {
      for (let row = bottom; row >= top; row--) {
        result.push(matrix[row][left]);
      }
      left++; // 왼쪽 경계 오른쪽으로 이동
    }
  }

  return result;
};
