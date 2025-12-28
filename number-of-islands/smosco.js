/**
 * Number of Islands - DFS 방식
 *
 * 문제: m x n 그리드에서 섬의 개수 구하기
 * - '1': 땅, '0': 물
 * - 섬: 상하좌우로 연결된 땅의 집합
 *
 * 접근 방법:
 * 1. 그리드를 순회하면서 '1'을 만나면 섬 발견 (count++)
 * 2. DFS로 연결된 모든 '1'을 '0'으로 바꿔서 방문 표시
 * 3. 다음 '1'을 찾으면 새로운 섬
 *
 * 시간복잡도: O(m * n) - 모든 셀을 최대 한 번씩 방문
 * 공간복잡도: O(m * n) - 최악의 경우 DFS 재귀 스택 (모든 칸이 땅일 때)
 *
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  if (!grid || grid.length === 0) return 0;

  const m = grid.length;
  const n = grid[0].length;
  let count = 0;

  // DFS로 연결된 모든 땅을 방문 처리
  const dfs = (i, j) => {
    // 범위 벗어나거나 물이면 종료
    if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] === '0') {
      return;
    }

    // 방문 처리 (땅을 물로 바꿈)
    grid[i][j] = '0';

    // 상하좌우 탐색
    dfs(i - 1, j); // 위
    dfs(i + 1, j); // 아래
    dfs(i, j - 1); // 왼쪽
    dfs(i, j + 1); // 오른쪽
  };

  // 그리드 전체 순회
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === '1') {
        count++; // 새로운 섬 발견
        dfs(i, j); // 연결된 모든 땅 방문 처리
      }
    }
  }

  return count;
};

// 테스트
if (require.main === module) {
  // Example 1
  const grid1 = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
  ];
  console.log(numIslands(grid1)); // 1

  // Example 2
  const grid2 = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
  ];
  console.log(numIslands(grid2)); // 3
}
