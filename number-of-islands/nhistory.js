var numIslands = function (grid) {
  // Declare row and column length
  const m = grid.length,
    n = grid[0].length;
  let numIslands = 0;

  // Available directions for depth-first search
  const dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  // Function to depth-first search inside of grid
  const dfs = (i, j) => {
    grid[i][j] = "2";

    let x, y;
    for (d of dir) {
      x = i + d[0];
      y = j + d[1];
      if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] === "1") {
        dfs(x, y);
      }
    }
    return;
  };

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === "1") {
        dfs(i, j);
        numIslands++;
      }
    }
  }
  return numIslands;
};

// TC: O(m*n)
// SC: O(m*n)
