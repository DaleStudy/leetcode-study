/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */

const directions = [
  [0, -1],
  [1, 0],
  [-1, 0],
  [0, 1],
];

var exist = function (board, word) {
  const cols = board[0].length; // 가로 (열 개수)
  const rows = board.length; // 세로 (행 개수)
  let res = false;

  for (let col = 0; col < cols; col++) {
    for (let row = 0; row < rows; row++) {
      if (board[row][col] != word[0]) continue;

      const visited = Array.from({ length: rows }, () =>
        Array(cols).fill(false)
      );
      if (res) break;
      dfs(row, col, board[row][col], visited);
    }
  }

  function check(row, col) {
    if (!(row >= 0 && row < rows)) return false;
    if (!(col >= 0 && col < cols)) return false;
    return true;
  }

  function dfs(row, col, str, visited) {
    if (str == word) {
      res = true;
      return;
    }
    if (str.length >= word.length) return;
    visited[row][col] = true;

    for (const direction of directions) {
      const [d_r, d_c] = direction;
      const newCol = col + d_c;
      const newRow = row + d_r;

      if (check(newRow, newCol) && !visited[newRow][newCol]) {
        dfs(newRow, newCol, str + board[newRow][newCol], visited);
      }
    }
    visited[row][col] = false;
  }

  return res;
};
