// TC: O(n), where N = total number of cells = m * n
// SC: O(n)

function numIslands(grid: string[][]): number {
  const sink = (row: number, col: number) => {
    visited[row][col] = true;

    const dirs = [
      [row - 1, col],
      [row + 1, col],
      [row, col - 1],
      [row, col + 1],
    ];

    for (const dir of dirs) {
      const [r, c] = dir;

      if (r >= 0 && r < grid.length && c >= 0 && c < grid[0].length) {
        if (!visited[r][c] && grid[r][c] === "1") {
          sink(r, c);
        }
      }
    }
  };

  let count = 0;
  const visited: boolean[][] = Array.from({ length: grid.length }, () =>
    Array(grid[0].length).fill(false)
  );

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (!visited[i][j] && grid[i][j] === "1") {
        count++;
        sink(i, j); // // Sink all connected neighboring land cells
      }
    }
  }

  return count;
}
