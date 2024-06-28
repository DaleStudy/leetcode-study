// Time Complexity: O(rows + cols)
// Space Complexity: O(rows + cols)

var pacificAtlantic = function (heights) {
  const rows = heights.length;
  const cols = heights[0].length;

  // initialize matrices to keep track of cells reachable by Pacific and Atlantic
  const pacific = [];
  const atlantic = [];

  // create 2D arrays filled with false values
  for (let i = 0; i < rows; i++) {
    pacific.push(new Array(cols).fill(false));
    atlantic.push(new Array(cols).fill(false));
  }

  // directions for moving up, right, down, left
  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  // helper to do DFS
  function dfs(row, col, ocean) {
    // mark the cell as reachable
    ocean[row][col] = true;
    for (const [dx, dy] of directions) {
      // check all 4 directions
      const newRow = row + dx;
      const newCol = col + dy;
      // continue if the new cell is within bounds, not visited, and has a height greater than or equal to the current cell
      if (
        newRow >= 0 &&
        newRow < rows &&
        newCol >= 0 &&
        newCol < cols &&
        !ocean[newRow][newCol] &&
        heights[newRow][newCol] >= heights[row][col]
      ) {
        dfs(newRow, newCol, ocean);
      }
    }
  }

  // start DFS from the Pacific ocean borders
  for (let i = 0; i < rows; i++) {
    // left edge
    dfs(i, 0, pacific);
    // right edge
    dfs(i, cols - 1, atlantic);
  }

  // start DFS from the Atlantic ocean borders
  for (let j = 0; j < cols; j++) {
    // top edge
    dfs(0, j, pacific);
    dfs(rows - 1, j, atlantic); // Bottom edge
  }

  const result = [];
  // check each cell can reach both oceans
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (pacific[i][j] && atlantic[i][j]) {
        // if it can reach both
        result.push([i, j]);
      }
    }
  }

  // return the final list
  return result;
};
