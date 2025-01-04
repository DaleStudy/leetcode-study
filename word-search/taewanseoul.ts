/**
 * 268. Missing Number
 * Given an m x n grid of characters board and a string word, return true if word exists in the grid.
 * The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
 *
 * https://leetcode.com/problems/word-search/description/
 */

// O(4^n) time
// O(n * m) space
function exist(board: string[][], word: string): boolean {
  let result = false;
  const num_rows = board.length;
  const num_cols = board[0].length;

  function checkNeighbors(
    board: (string | null)[][],
    word: string,
    row: number,
    col: number,
    startIndex: number
  ) {
    const num_rows = board.length;
    const num_cols = board[0].length;

    if (row < 0 || row >= num_rows || col < 0 || col >= num_cols) return;

    if (board[row][col] !== word[startIndex]) return;

    if (startIndex === word.length - 1) {
      result = true;
      return;
    }

    board[row][col] = null;
    checkNeighbors(board, word, row + 1, col, startIndex + 1);
    checkNeighbors(board, word, row - 1, col, startIndex + 1);
    checkNeighbors(board, word, row, col + 1, startIndex + 1);
    checkNeighbors(board, word, row, col - 1, startIndex + 1);
    board[row][col] = word[startIndex];
  }

  for (let i = 0; i < num_rows; i++) {
    for (let j = 0; j < num_cols; j++) {
      if (board[i][j] === word[0]) {
        checkNeighbors(board, word, i, j, 0);
        if (result) return result;
      }
    }
  }

  return result;
}
