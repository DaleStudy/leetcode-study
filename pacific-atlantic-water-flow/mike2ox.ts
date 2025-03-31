/**
 * Source: https://leetcode.com/problems/pacific-atlantic-water-flow/
 * 풀이방법: DFS를 이용하여 pacific과 atlantic에서 물이 흐르는 지점을 찾음
 *
 * 시간복잡도: O(n * m) (n: 행의 개수, m: 열의 개수)
 * 공간복잡도: O(n * m)
 */

function pacificAtlantic(heights: number[][]): number[][] {
  if (!heights || !heights[0]) return [];

  const rows = heights.length;
  const cols = heights[0].length;

  // checklist
  const pacific = new Set<string>();
  const atlantic = new Set<string>();

  // DFS
  function dfs(
    row: number,
    col: number,
    prevHeight: number,
    visited: Set<string>
  ) {
    // row, col이 경계 밖이거나 이미 방문했거나 이전 높이보다 낮은 경우
    if (
      row < 0 ||
      row >= rows ||
      col < 0 ||
      col >= cols ||
      heights[row][col] < prevHeight ||
      visited.has(`${row},${col}`)
    ) {
      return;
    }

    // 현재 위치 체크
    visited.add(`${row},${col}`);

    // 4방향 탐색
    dfs(row + 1, col, heights[row][col], visited);
    dfs(row - 1, col, heights[row][col], visited);
    dfs(row, col + 1, heights[row][col], visited);
    dfs(row, col - 1, heights[row][col], visited);
  }

  // 0,0에서부터 탐색 시작
  for (let col = 0; col < cols; col++) {
    dfs(0, col, heights[0][col], pacific);
  }
  for (let row = 0; row < rows; row++) {
    dfs(row, 0, heights[row][0], pacific);
  }

  // rows-1, cols-1(pacific하고는 정반대 위치에서 시작)
  for (let col = 0; col < cols; col++) {
    dfs(rows - 1, col, heights[rows - 1][col], atlantic);
  }
  for (let row = 0; row < rows; row++) {
    dfs(row, cols - 1, heights[row][cols - 1], atlantic);
  }

  const result: number[][] = [];
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      const pos = `${row},${col}`;
      if (pacific.has(pos) && atlantic.has(pos)) {
        result.push([row, col]);
      }
    }
  }

  return result;
}
