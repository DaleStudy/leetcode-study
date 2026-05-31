// Time Complexity: O(m * n)
// Space Complexity: O(m * n)

const pacificAtlantic = (heights) => {
  if (!heights?.length || !heights[0]?.length) {
    return [];
  }

  const m = heights.length;
  const n = heights[0].length;
  const pacific = Array.from({ length: m }, () => Array(n).fill(false));
  const atlantic = Array.from({ length: m }, () => Array(n).fill(false));
  const dirs = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  const dfs = (visited, r, c) => {
    visited[r][c] = true;
    for (const [dr, dc] of dirs) {
      const nr = r + dr;
      const nc = c + dc;
      if (nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc]) continue;
      if (heights[nr][nc] < heights[r][c]) continue;
      dfs(visited, nr, nc);
    }
  };

  for (let i = 0; i < m; i++) {
    dfs(pacific, i, 0);
    dfs(atlantic, i, n - 1);
  }
  for (let j = 0; j < n; j++) {
    dfs(pacific, 0, j);
    dfs(atlantic, m - 1, j);
  }

  const result = [];
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (pacific[r][c] && atlantic[r][c]) {
        result.push([r, c]);
      }
    }
  }
  return result;
};
