/**
 * https://leetcode.com/problems/set-matrix-zeroes/
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
  const m = matrix.length;
  const n = matrix[0].length;

  let firstRowHasZero = false;
  let firstColHasZero = false;

  // 1. 첫 번째 열에 0이 있는지 확인
  for (let i = 0; i < m; i++) {
    if (matrix[i][0] === 0) {
      firstColHasZero = true;
      break;
    }
  }

  // 2. 첫 번째 행에 0이 있는지 확인
  for (let j = 0; j < n; j++) {
    if (matrix[0][j] === 0) {
      firstRowHasZero = true;
      break;
    }
  }

  // 3. 나머지 matrix에서 0을 찾고, 첫 행/열에 마킹
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (matrix[i][j] === 0) {
        matrix[i][0] = 0; // i번째 행에 0 마킹
        matrix[0][j] = 0; // j번째 열에 0 마킹
      }
    }
  }

  // 4. 마킹을 기준으로 행과 열을 0으로 변경
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      if (matrix[i][0] === 0 || matrix[0][j] === 0) {
        matrix[i][j] = 0;
      }
    }
  }

  // 5. 첫 번째 행을 0으로 설정
  if (firstRowHasZero) {
    for (let j = 0; j < n; j++) {
      matrix[0][j] = 0;
    }
  }

  // 6. 첫 번째 열을 0으로 설정
  if (firstColHasZero) {
    for (let i = 0; i < m; i++) {
      matrix[i][0] = 0;
    }
  }
};
