/**
 * TC: O(ROW * COLUMN)
 * SC: O(1)
 */

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
  const ROW = matrix.length;
  const COLUMN = matrix[0].length;
  const MARK = "#";

  // 1. 0인 요소의 가로, 세로를 특정문자로 변경
  for (let row = 0; row < ROW; row++) {
    for (let column = 0; column < COLUMN; column++) {
      if (matrix[row][column] === 0) {
        changeToMark(row, column);
      }
    }
  }

  // 2. 특정문자를 모두 0으로 변경
  for (let row = 0; row < ROW; row++) {
    for (let column = 0; column < COLUMN; column++) {
      if (matrix[row][column] === MARK) {
        matrix[row][column] = 0;
      }
    }
  }

  // 3. 특정 좌표의 가로, 세로를 char문자로 변경 (대신 0인 요소는 변경하지 않음)
  function changeToMark(row, column) {
    for (let r = 0; r < ROW; r++) {
      if (matrix[r][column] !== 0) {
        matrix[r][column] = MARK;
      }
    }
    for (let c = 0; c < COLUMN; c++) {
      if (matrix[row][c] !== 0) {
        matrix[row][c] = MARK;
      }
    }
  }
};
