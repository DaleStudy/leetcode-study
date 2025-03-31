/**
 * @param {number[][]} heights
 * @return {number[][]}
 */

// ✅ Time Complexity: O(m * n)
// ✅ Space Complexity: O(m * n)

var pacificAtlantic = function (heights) {
  const m = heights.length;
  const n = heights[0].length;

  // ❌ Array(m).fill(Array(n).fill(false)) → Incorrect (all rows share the same array)
  const pacific = Array.from({ length: m }, () => Array(n).fill(false));
  const atlantic = Array.from({ length: m }, () => Array(n).fill(false));

  // four possible movement directions: down, up, right, left
  const directions = [
    [1, 0], // ⬇️
    [-1, 0], // ⬆️
    [0, 1], // ➡️
    [0, -1], // ⬅️
  ];

  /**
   * Depth-First Search (DFS) to mark reachable cells
   * @param {number} row - current row index
   * @param {number} col - current column index
   * @param {boolean[][]} visited - visited cells
   * @param {number} prevHeight - previously visited cell's height
   */

  const dfs = (row, col, visited, prevHeight) => {
    // No search needed:
    // 1) Out of bounds
    // 2) already visited
    // 3) current height < previous height
    if (
      row < 0 ||
      row >= m ||
      col < 0 ||
      col >= n ||
      visited[row][col] ||
      heights[row][col] < prevHeight
    ) {
      return;
    }

    // mark current cell as visited
    visited[row][col] = true;

    // visit all four possible directions
    for (const [dr, dc] of directions) {
      dfs(row + dr, col + dc, visited, heights[row][col]);
    }
  };

  // start dfs from each border
  for (let i = 0; i < m; i++) {
    dfs(i, 0, pacific, heights[i][0]); // left border(Pacific ocean)
    dfs(i, n - 1, atlantic, heights[i][n - 1]); // right border(Atlantic ocean)
  }

  for (let j = 0; j < n; j++) {
    dfs(0, j, pacific, heights[0][j]); // top border(Pacific ocean)
    dfs(m - 1, j, atlantic, heights[m - 1][j]); // bottom border(Atlantic ocean)
  }

  let result = [];

  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (pacific[r][c] && atlantic[r][c]) {
        result.push([r, c]);
      }
    }
  }
  return result;
};

// Example test
const heights = [
  [1, 2, 2, 3, 5],
  [3, 2, 3, 4, 4],
  [2, 4, 5, 3, 1],
  [6, 7, 1, 4, 5],
  [5, 1, 1, 2, 4],
];

const expected = [
  [0, 4],
  [1, 3],
  [1, 4],
  [2, 2],
  [3, 0],
  [3, 1],
  [4, 0],
];

const output = pacificAtlantic(heights);

if (JSON.stringify(output.sort()) === JSON.stringify(expected.sort())) {
  console.log("✅ Accepted\n");
} else {
  console.log("❌ Not Accepted\n");
}

console.log("Input:", heights, "\n");
console.log("Output:", output, "\n");
console.log("Expected:", expected);

