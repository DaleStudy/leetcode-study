/**
 * @param heights - 셀의 해발고도 배열
 * @returns
 * @description
 * - 인접한 셀의 높이가 작거나 같으면 빗물이 흐를 수 있음
 * - 바다에 인접한 셀에서는 바다로 물이 흐를 수 있음
 * - 태평양과 대서양 모두로 흐를 수 있는 경로 반환
 * - 결국 [0, n] 과 [m, 0]는 반드시 포함
 *
 * 1. 역순으로 가는게 유리하다는 힌트를 채택
 * 2. 모든 셀의 이동 가능 방향을 파악 (dfs, bfs)
 */

function pacificAtlantic(heights: number[][]): number[][] {
  const yMax = heights.length;
  const xMax = heights[0].length;

  // 태평양, 대서양의 visit 체크를 위한 set
  const pacific = new Set<string>();
  const atlantic = new Set<string>();

  const result: number[][] = [];
  function dfs(y: number, x: number, visited: Set<string>, prevHeight: number) {
    const key = `${y},${x}`;

    if (
      x < 0 ||
      x >= xMax ||
      y < 0 ||
      y >= yMax ||
      visited.has(key) ||
      prevHeight > heights[y][x]
    ) {
      return;
    }

    visited.add(key);
    dfs(y, x + 1, visited, heights[y][x]);
    dfs(y, x - 1, visited, heights[y][x]);
    dfs(y + 1, x, visited, heights[y][x]);
    dfs(y - 1, x, visited, heights[y][x]);
  }

  // 맨 양 끝쪽을 dfs의 시작점으로 지정
  for (let i = 0; i < yMax; i++) {
    dfs(i, 0, pacific, heights[i][0]);
    dfs(i, xMax - 1, atlantic, heights[i][xMax - 1]);
  }

  for (let j = 0; j < xMax; j++) {
    dfs(0, j, pacific, heights[0][j]);
    dfs(yMax - 1, j, atlantic, heights[yMax - 1][j]);
  }

  // 유니온 값 체크
  for (let i = 0; i < yMax; i++) {
    for (let j = 0; j < xMax; j++) {
      const key = `${i},${j}`;

      if (pacific.has(key) && atlantic.has(key)) {
        result.push([i, j]);
      }
    }
  }

  return result;
}

const heights = [
  [1, 2, 2, 3, 5],
  [3, 2, 3, 4, 4],
  [2, 4, 5, 3, 1],
  [6, 7, 1, 4, 5],
  [5, 1, 1, 2, 4],
];

pacificAtlantic(heights);

// 태 평 양 (Pacific)
//   ~ ~ ~ ~ ~ ~
// ~ [1] [2] [2] [3] (5) ~  <-- 오른쪽/아래는 대서양
// ~ [3] [2] [3] (4) (4) ~
// ~ [2] [4] (5) [3] [1] ~
// ~ (6) (7) (1) [4] [5] ~
// ~ (5) [1] [1] [2] [4] ~
//           ~ ~ ~ ~ ~ ~
//           대 서 양 (Atlantic)


