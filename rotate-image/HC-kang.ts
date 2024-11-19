/**
 * https://leetcode.com/problems/rotate-image
 * T.C. O(n^2)
 * S.C. O(1)
 */
function rotate(matrix: number[][]): void {
  const n = matrix.length;

  // transpose
  for (let i = 0; i < n; i++) {
    for (let j = i; j < n; j++) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
  }

  // reverse
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n / 2; j++) {
      [matrix[i][j], matrix[i][n - j - 1]] = [matrix[i][n - j - 1], matrix[i][j]];
    }
  }
}
