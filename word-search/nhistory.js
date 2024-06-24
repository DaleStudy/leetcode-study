var exist = function (board, word) {
  const dfs = (row, col, index) => {
    if (word.length === index) return true;
    if (
      row < 0 ||
      col < 0 ||
      row >= board.length ||
      col >= board[0].length ||
      board[row][col] !== word[index]
    )
      return false;

    board[row][col] = "#";
    if (
      dfs(row + 1, col, index + 1) ||
      dfs(row, col + 1, index + 1) ||
      dfs(row - 1, col, index + 1) ||
      dfs(row, col - 1, index + 1)
    )
      return true;

    board[row][col] = word[index];
  };

  for (let row = 0; row < board.length; row++) {
    for (let col = 0; col < board[row].length; col++) {
      if (board[row][col] === word[0] && dfs(row, col, 0)) return true;
    }
  }

  return false;
};

// N: board column length / M: board row length / L: word length
// TC: O(N*M*4^L)
// SC: O(L)
