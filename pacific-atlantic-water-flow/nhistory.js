/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function (heights) {
  const m = heights.length,
    n = heights[0].length;
  let result = [];

  const pacific = new Array(m).fill(null).map(() => new Array(n).fill(false));
  const atlantic = new Array(m).fill(null).map(() => new Array(n).fill(false));

  const dir = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  const dfs = (i, j, ocean) => {
    // Check visited cell
    ocean[i][j] = true;

    for (d of dir) {
      let x = i + d[0],
        y = j + d[1];
      if (
        x >= 0 &&
        x < m &&
        y >= 0 &&
        y < n &&
        !ocean[x][y] &&
        heights[x][y] >= heights[i][j]
      ) {
        dfs(x, y, ocean);
      }
    }
  };

  // Check the cells can flow left and right edge
  for (let i = 0; i < m; i++) {
    dfs(i, 0, pacific);
    dfs(i, n - 1, atlantic);
  }

  // Check the cells can flow top and bottom edge
  for (let j = 0; j < n; j++) {
    dfs(0, j, pacific);
    dfs(m - 1, j, atlantic);
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (pacific[i][j] && atlantic[i][j]) {
        result.push([i, j]);
      }
    }
  }
  return result;
};

// TC: O(m*n)
// SC: O(m*n)
