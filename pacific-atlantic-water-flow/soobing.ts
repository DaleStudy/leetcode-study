/**
 * 문제 설명
 * - 비가 내렸을 때, 태평양과 대서양 모두로 물이 흐를 수 있는 지점을 찾아 반환하는 문제입니다.
 * 아이디어
 * 1) BFS/DFS
 * - 각 바다에서 역방향으로 물이 도달할 수 있는 셀을 탐색한 후, 두 바다 모두에 도달 가능한 셀의 교집합 구하기
 *
 */

function pacificAtlantic(heights: number[][]): number[][] {
  const m = heights.length;
  const n = heights[0].length;

  const pacific = Array.from({ length: m }, () => Array(n).fill(false));
  const atlantic = Array.from({ length: m }, () => Array(n).fill(false));

  const directions = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];

  function dfs(r: number, c: number, visited: boolean[][], prevHeight: number) {
    if (
      r < 0 ||
      c < 0 ||
      r >= m ||
      c >= n ||
      visited[r][c] ||
      heights[r][c] < prevHeight
    )
      return;

    visited[r][c] = true;

    for (const [dr, dc] of directions) {
      dfs(r + dr, c + dc, visited, heights[r][c]);
    }
  }

  // 태평양 DFS
  for (let i = 0; i < m; i++) {
    dfs(i, 0, pacific, heights[i][0]); // 왼쪽
    dfs(i, n - 1, atlantic, heights[i][n - 1]); // 오른쪽
  }

  for (let j = 0; j < n; j++) {
    dfs(0, j, pacific, heights[0][j]); // 위쪽
    dfs(m - 1, j, atlantic, heights[m - 1][j]); // 아래쪽
  }

  const result: number[][] = [];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (pacific[i][j] && atlantic[i][j]) {
        result.push([i, j]);
      }
    }
  }

  return result;
}
