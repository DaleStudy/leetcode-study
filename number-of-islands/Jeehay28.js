/**
 * @param {character[][]} grid
 * @return {number}
 */

// 🌻
// Time Complexity: O(m * n), where M is the number of rows and N is the number of columns in the grid.
// Space Complexity: O(k), where k is the size of the largest island (k <= m * n)

// The space complexity is determined by the depth of the recursive stack used by the sink function.
// In the worst-case scenario, where the entire grid is filled with "1"s (a single large island),
// the depth of recursion could go up to O(m * n).

var numIslands = function (grid) {
  // depth-first search (DFS) that potentially visits every connected cell in the current island
  const sink = (row, col) => {
    grid[row][col] = "0";

    const adjacent = [
      [row - 1, col], // up
      [row + 1, col], // down
      [row, col - 1], // left
      [row, col + 1], // right
    ];

    for ([r, c] of adjacent) {
      if (r >= 0 && r < grid.length && c >= 0 && c < grid[r].length) {
        if (grid[r][c] === "1") {
          sink(r, c);
        }
      }
    }
  };

  let cnt = 0;

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === "1") {
        cnt += 1;
        sink(i, j);
      }
    }
  }

  return cnt;
};



