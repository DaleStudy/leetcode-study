// TC: O(M * N * 4^W)
// SC: O(MIN)
// W: word.length, MIN: min(M * N, W)

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  let result = false;

  for (let r = 0; r < board.length; r++) {
    for (let c = 0; c < board[0].length; c++) {
      dfs(r, c, 0);
    }
  }

  return result;

  function dfs(row, column, wordIndex) {
    if (!isValid(row, column)) {
      return;
    }
    if (board[row][column] !== word[wordIndex]) {
      return;
    }
    if (wordIndex === word.length - 1) {
      result = true;
      return;
    }

    const temp = board[row][column];
    board[row][column] = "#";
    dfs(row + 1, column, wordIndex + 1);
    dfs(row - 1, column, wordIndex + 1);
    dfs(row, column + 1, wordIndex + 1);
    dfs(row, column - 1, wordIndex + 1);
    board[row][column] = temp;
  }

  function isValid(row, column) {
    if (row < 0 || board.length <= row) {
      return false;
    }
    if (column < 0 || board[0].length <= column) {
      return false;
    }
    return true;
  }
};
