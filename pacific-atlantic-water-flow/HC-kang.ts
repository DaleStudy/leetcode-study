/**
 * https://leetcode.com/problems/pacific-atlantic-water-flow
 * T.C. O((m * n)^2)
 * S.C. O(m * n)
 */
function pacificAtlantic(heights: number[][]): number[][] {
  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  function pacificDfs(row: number, col: number, visited: Set<string>) {
    const key = `${row},${col}`;
    if (visited.has(key)) return;
    visited.add(key);

    if (row === 0 || col === 0) {
      // left or top
      return true;
    }

    for (let [r, c] of dir) {
      if (row + r < 0 || row + r >= heights.length) continue;
      if (col + c < 0 || col + c >= heights[0].length) continue;
      if (heights[row][col] < heights[row + r][col + c]) continue;
      if (pacificDfs(row + r, col + c, visited)) return true;
    }
    return false;
  }

  function atlanticDfs(row: number, col: number, visited: Set<string>) {
    const key = `${row},${col}`;
    if (visited.has(key)) return;
    visited.add(key);

    if (row === heights.length - 1 || col === heights[0].length - 1) {
      // right or bottom
      return true;
    }

    for (let [r, c] of dir) {
      if (row + r < 0 || row + r >= heights.length) continue;
      if (col + c < 0 || col + c >= heights[0].length) continue;
      if (heights[row][col] < heights[row + r][col + c]) continue;
      if (atlanticDfs(row + r, col + c, visited)) return true;
    }
    return false;
  }

  const result: number[][] = [];
  for (let i = 0; i < heights.length; i++) {
    for (let j = 0; j < heights[0].length; j++) {
      if (
        pacificDfs(i, j, new Set<string>()) &&
        atlanticDfs(i, j, new Set<string>())
      ) {
        result.push([i, j]);
      }
    }
  }

  return result;
}

/**
 * T.C. O(m * n)
 * S.C. O(m * n)
 */
function pacificAtlantic(heights: number[][]): number[][] {
  const pacific: Set<string> = new Set();
  const atlantic: Set<string> = new Set();

  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  function dfs(row: number, col: number, visited: Set<string>) {
    const key = `${row},${col}`;
    if (visited.has(key)) return;
    visited.add(key);

    for (let [r, c] of dir) {
      if (row + r < 0 || row + r >= heights.length) continue;
      if (col + c < 0 || col + c >= heights[0].length) continue;
      if (heights[row][col] > heights[row + r][col + c]) continue;
      dfs(row + r, col + c, visited);
    }
  }

  for (let i = 0; i < heights.length; i++) {
    dfs(i, 0, pacific);
    dfs(i, heights[0].length - 1, atlantic);
  }

  for (let i = 0; i < heights[0].length; i++) {
    dfs(0, i, pacific);
    dfs(heights.length - 1, i, atlantic);
  }

  const result: number[][] = [];

  for (const p of pacific) {
    if (atlantic.has(p)) {
      const [row, col] = p.split(',').map(Number);
      result.push([row, col]);
    }
  }

  return result;
}
