/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  if (!grid || grid.length === 0) return 0;

  const rows = grid.length;
  const cols = grid[0].length;
  let islandCount = 0;

  const dfs = (row, col) => {
    if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] === '0') {
      return;
    }

    grid[row][col] = '0';

    dfs(row - 1, col);
    dfs(row + 1, col);
    dfs(row, col - 1);
    dfs(row, col + 1);
  };

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (grid[i][j] === '1') {
        islandCount++;
        dfs(i, j);
      }
    }
  }

  return islandCount;
};
