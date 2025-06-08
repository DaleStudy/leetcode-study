// TC: O(m * n)
// SC: O(m * n)

function pacificAtlantic(heights: number[][]): number[][] {
  const m = heights.length;
  const n = heights[0].length;

  const pacific: boolean[][] = Array.from({ length: m }, () =>
    Array(n).fill(false)
  );
  const atlantic: boolean[][] = Array.from({ length: m }, () =>
    Array(n).fill(false)
  );

  const directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  const dfs = (row: number, col: number, visited: boolean[][]) => {
    visited[row][col] = true;
    // Border cells are adjacent to the ocean, so they are marked as reachable (true)

    // From each ocean-border cell, we explore inward:
    // if an adjacent cell is higher or equal, water can flow from it to the ocean
    // → mark it as reachable (true)
    for (const [dr, dc] of directions) {
      const newRow = row + dr;
      const newCol = col + dc;

      if (
        newRow >= 0 &&
        newRow < m &&
        newCol >= 0 &&
        newCol < n &&
        !visited[newRow][newCol] &&
        heights[row][col] <= heights[newRow][newCol]
        // heights[row][col] <= heights[newRow][newCol]
        // → Water can flow from (newRow, newCol) to (row, col),
        // so (row, col) is reachable from the ocean through (newRow, newCol)
      ) {
        dfs(newRow, newCol, visited);
      }
    }
  };

  for (let i = 0; i < m; i++) {
    dfs(i, 0, pacific);
    dfs(i, n - 1, atlantic);
  }

  for (let j = 0; j < n; j++) {
    dfs(0, j, pacific);
    dfs(m - 1, j, atlantic);
  }

  let result: number[][] = [];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (pacific[i][j] && atlantic[i][j]) {
        result.push([i, j]);
      }
    }
  }

  return result;
}

