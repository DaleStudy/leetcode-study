
/**
 * Time Complexity: O(m * n * 4^k)
 * Space Complexity: O(m * n)
 */
function exist(board: string[][], word: string): boolean {
  // Initialize the board dimensions
  const m = board.length;
  const n = board[0].length;

  const dfs = (i: number, j: number, index: number): boolean => {
    // If we've matched all characters, return true
    if (index === word.length) return true;
    // If out of bounds or current character doesn't match, return false
    if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] !== word[index]) return false;

    // Temporarily mark the current cell as visited
    const temp = board[i][j];
    board[i][j] = '#';

    // Explore all four possible directions
    const found =
      dfs(i + 1, j, index + 1) ||
      dfs(i - 1, j, index + 1) ||
      dfs(i, j + 1, index + 1) ||
      dfs(i, j - 1, index + 1);

    // Unmark the current cell (backtracking)
    board[i][j] = temp;

    // Return true if we found the word
    return found;
  };

  // Iterate through each cell in the board
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      // Start DFS from each cell
      if (dfs(i, j, 0)) return true;
    }
  }

  // If we didn't find the word, return false
  return false;
}