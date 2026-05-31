/**
 * @param grid - 섬(1), 물(0)로 이뤄진 m * n 2차원 배열
 * @returns - 섬의 갯수 (연결되지 않으면 개별 섬)
 * @description
 * - dfs 까진 알았는데 AI의 도움을 받았음
 * - 탐색 문제에서 디테일까지 접근하는 연습이 필요
 * - 시간 복잡도 O(M * N)
 */

function numIslands(grid: string[][]): number {
  const visit = Array.from({ length: grid.length }, () =>
    Array.from({ length: grid[0].length }, () => false)
  );

  const moveY = [0, 0, -1, 1];
  const moveX = [-1, 1, 0, 0];

  let cnt = 0;
  function dfs(y: number, x: number) {
    visit[y][x] = true;
    // 4 방향 index 확인
    for (let i = 0; i < 4; i++) {
      const nextY = y + moveY[i];
      const nextX = x + moveX[i];

      if (
        nextX >= 0 &&
        nextY >= 0 &&
        nextX < grid[0].length &&
        nextY < grid.length &&
        grid[nextY][nextX] === "1" &&
        !visit[nextY][nextX]
      ) {
        dfs(nextY, nextX);
      }
    }
  }

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === "1" && !visit[i][j]) {
        cnt++;
        dfs(i, j);
      }
    }
  }

  return cnt;
}

const grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"],
];
numIslands(grid);


