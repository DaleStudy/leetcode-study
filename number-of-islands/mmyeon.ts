/**
 *@link https://leetcode.com/problems/number-of-islands/
 *
 * 접근 방법 :
 *  - 섬의 시작점에서 끝까지 탐색해야 하므로 DFS 사용
 *  - 방문한 섬은 중복 탐색 방지하기 위해서 방문 후 값 변경 처리
 *
 * 시간복잡도 : O(m * n)
 *  - 2차원 배열 전체를 순회하므로 O(m * n)
 *
 * 공간복잡도 : O(m * n)
 *  - DFS 호출 스택 최대 깊이가 m * n 만큼 쌓일 수 있다.
 */

function numIslands(grid: string[][]): number {
  let count = 0;
  const rows = grid.length;
  const cols = grid[0].length;

  // 상하좌우 탐색 방향 배열
  const directions = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0],
  ];

  // 현재 위치에서 연결된 모든 섬 탐색
  const dfs = (row: number, col: number) => {
    // 종료 조건 : 범위 벗어나거나, 이미 방문한 경우
    if (
      row < 0 ||
      row >= rows ||
      col < 0 ||
      col >= cols ||
      grid[row][col] === "0"
    )
      return;

    // 현재 위치 방문 처리
    grid[row][col] = "0";

    // 상하좌우 탐색
    for (const [x, y] of directions) {
      dfs(row + x, col + y);
    }
  };

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      // 섬의 시작점인 경우
      if (grid[row][col] === "1") {
        count++;
        dfs(row, col);
      }
    }
  }

  return count;
}
