// Time Complexity: O(m * n)
// Space Complexity: O(m * n)

var numIslands = function (grid) {
  const m = grid.length;
  const n = grid[0].length;
  let numIslands = 0;

  // directions arrays for moving up, down, left, and right
  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  // BFS function
  function bfs(row, col) {
    const queue = [[row, col]];
    // mark as visited
    grid[row][col] = "0";

    while (queue.length > 0) {
      const [r, c] = queue.shift();

      for (const [dr, dc] of directions) {
        const nr = r + dr;
        const nc = c + dc;

        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] === "1") {
          // mark as visited
          grid[nr][nc] = "0";
          queue.push([nr, nc]);
        }
      }
    }
  }

  // iterate through each cell in the grid
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === "1") {
        numIslands++;
        // start BFS to mark all connected land cells
        bfs(i, j);
      }
    }
  }

  return numIslands;
};
