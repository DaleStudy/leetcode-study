/**
 * @link https://leetcode.com/problems/pacific-atlantic-water-flow/description/
 *
 * 접근 방법 :
 * - pacific, atlantic를 동시에 도달하는 지점 찾기 위해서, 도달 여부 트래킹하는 2개의 visited 배열 사용한다.
 * - 바다 경계에서만 DFS를 호출해서 방문 여부 체크한다.
 * - 바다 경계에서 시작했기 때문에 DFS는 인접 셀의 높이가 같거나 높을 때만 호출되어야 한다.
 *
 * 시간복잡도 : O(m * n)
 *  - 각 셀마다 최대 4번 DFS가 호출될 수 있다. O(m * n)
 *  - 결과 순회할 때 m * n 만큼 순회한다.
 *
 * 공간복잡도 : O(m * n)
 *  - 2개의 visited 배열 사용한다.
 *  - 최악의 경우, m * n 모든 칸에서 DFS 호출된다.
 */

const directions = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];

function pacificAtlantic(heights: number[][]): number[][] {
  const result: number[][] = [];

  const rows = heights.length;
  const cols = heights[0].length;

  // 두 바다 도달하는 지점 트래킹 하기 위한 배열
  const pacificVisited = Array.from({ length: rows }, () =>
    Array(cols).fill(false)
  );
  const atlanticVisited = Array.from({ length: rows }, () =>
    Array(cols).fill(false)
  );

  const dfs = (row: number, col: number, visited: boolean[][]) => {
    if (visited[row][col]) return;
    // 방문 지점 기록
    visited[row][col] = true;

    for (const [x, y] of directions) {
      const newRow = row + x;
      const newCol = col + y;

      // 새로운 위치가 경계안에 있고, 현재 높이보다 같거나 높을 때만 DFS 호출
      if (
        0 <= newRow &&
        newRow < rows &&
        0 <= newCol &&
        newCol < cols &&
        heights[newRow][newCol] >= heights[row][col]
      )
        dfs(newRow, newCol, visited);
    }
  };

  // pacific 경계에서 DFS 호출 (첫 번쨰 열, 첫 번째 행)
  for (let row = 0; row < rows; row++) dfs(row, 0, pacificVisited);
  for (let col = 0; col < cols; col++) dfs(0, col, pacificVisited);

  // atlantic 경계에서 DFS 호출 (마지막 열, 마지막 행)
  for (let row = 0; row < rows; row++) dfs(row, cols - 1, atlanticVisited);
  for (let col = 0; col < cols; col++) dfs(rows - 1, col, atlanticVisited);

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (pacificVisited[row][col] && atlanticVisited[row][col])
        result.push([row, col]);
    }
  }

  return result;
}
