// Time Complexity: O(m * n * 4^L), where L is the length of the word
// Space Complexity: O(L) due to he recursive call stack

function exist(board: string[][], word: string): boolean {
  // input: m * n grid of characters board, a string word
  // output: true if word exists in the grid

  const dfs = (index: number, row: number, col: number) => {
    if (
      row < 0 ||
      row >= board.length ||
      col < 0 ||
      col >= board[0].length ||
      board[row][col] !== word[index]
    ) {
      return false;
    }

    if (index === word.length - 1) {
      return true;
    }

    const visited = board[row][col];
    board[row][col] = "#";

    const result =
      dfs(index + 1, row + 1, col) ||
      dfs(index + 1, row - 1, col) ||
      dfs(index + 1, row, col + 1) ||
      dfs(index + 1, row, col - 1);

    board[row][col] = visited;

    return result;
  };

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (dfs(0, i, j)) {
        return true;
      }
    }
  }

  return false;
}
