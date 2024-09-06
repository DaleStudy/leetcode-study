//time-complexity : O(4^(ROWS*COLS))
//space-complexity : O(word.length)

const exist = function (board, word) {
  const ROWS = board.length;
  const COLS = board[0].length;

  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      if (board[r][c] === word[0]) {
        if (dfs(board, word, r, c, 0)) return true;
      }
    }
  }

  return false;
};

const dfs = function (board, word, r, c, i) {
  const ROWS = board.length;
  const COLS = board[0].length;

  if (r < 0 || r >= ROWS || c < 0 || c >= COLS || board[r][c] !== word[i]) {
    return false;
  }

  if (i === word.length - 1) return true;

  const temp = board[r][c];
  board[r][c] = null;

  let found =
    dfs(board, word, r + 0, c + 1, i + 1) ||
    dfs(board, word, r + 1, c + 0, i + 1) ||
    dfs(board, word, r + 0, c + -1, i + 1) ||
    dfs(board, word, r + -1, c + 0, i + 1);
  //forEach로 했더니 runtime 두 배 됨;;

  board[r][c] = temp;

  return found;
};
