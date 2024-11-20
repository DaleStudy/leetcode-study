/**
 * 전치(행과 열을 교환) 후 행 반전(뒤집기)
 *
 * TC: O(N^2)
 * SC: O(1)
 */

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
  const N = matrix.length;

  for (let row = 0; row < N; row++) {
    for (let column = row; column < N; column++) {
      [matrix[row][column], matrix[column][row]] = [
        matrix[column][row],
        matrix[row][column],
      ];
    }
  }

  for (let row = 0; row < N; row++) {
    matrix[row].reverse();
  }
};
