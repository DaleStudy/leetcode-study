/**
 * Runtime: 239ms, Memory: 51.98MB
 *
 * Time Complexity: O(rows * cols * 4^L) L: 단어 길이
 * Space Complexity: O(L)
 *
 */
function exist(board: string[][], word: string): boolean {
  const ROWS = board.length;
  const COLUMNS = board[0].length;

  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLUMNS; c++) {
      if (board[r][c] === word[0]) {
        if (check(r, c, 0, board, word)) return true;
      }
    }
  }

  return false;
}

function check(
  r: number,
  c: number,
  i: number,
  board: string[][],
  word: string
): boolean {
  const ROWS = board.length;
  const COLUMNS = board[0].length;

  if (i === word.length) {
    return true;
  }

  if (r < 0 || r >= ROWS || c < 0 || c >= COLUMNS || board[r][c] !== word[i]) {
    return false;
  }

  const temp = board[r][c];
  board[r][c] = "#";

  const found =
    check(r - 1, c, i + 1, board, word) || // 위
    check(r, c + 1, i + 1, board, word) || // 오른쪽
    check(r + 1, c, i + 1, board, word) || // 아래
    check(r, c - 1, i + 1, board, word); // 왼쪽

  board[r][c] = temp;

  return found;
}
