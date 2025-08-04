/**
 * 그래프 역방향 탐색 : DFS를 사용하여 태평양과 대서양에 도달할 수 있는 모든 지점을 찾는 문제
 * 시간 복잡도: O(m × n) - 각 셀을 최대 2번 방문
 * 공간 복잡도: O(m × n) - visited 배열과 스택 공간
 */
/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function (heights) {
  if (!heights || heights.length === 0) return [];

  const m = heights.length;
  const n = heights[0].length;

  // 비트마스킹 사용한 방문 상태 관리
  // 0: 미방문, 1: 태평양만, 2: 대서양만, 3: 둘 다
  const visited = Array(m)
    .fill()
    .map(() => Array(n).fill(0));
  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  const result = [];

  // DFS - 스택 사용
  function dfs(startPoints, oceanMask) {
    const stack = [...startPoints];

    while (stack.length > 0) {
      const [row, col] = stack.pop();

      // 이미 해당 바다로 표시되어 있으면 건너뛰기
      if (visited[row][col] & oceanMask) continue;

      // 현재 바다 표시
      visited[row][col] |= oceanMask;

      // 양쪽 바다 모두 도달 가능하면 결과에 추가
      if (visited[row][col] === 3) {
        result.push([row, col]);
      }

      // 4방향 탐색
      for (const [dr, dc] of directions) {
        const newRow = row + dr;
        const newCol = col + dc;

        // 경계 확인 및 높이 조건 확인
        if (
          newRow >= 0 &&
          newRow < m &&
          newCol >= 0 &&
          newCol < n &&
          heights[newRow][newCol] >= heights[row][col] &&
          !(visited[newRow][newCol] & oceanMask)
        ) {
          stack.push([newRow, newCol]);
        }
      }
    }
  }

  // 태평양 시작점들
  const pacificStarts = [];
  for (let i = 0; i < m; i++) pacificStarts.push([i, 0]); // 첫 번째 열
  for (let j = 1; j < n; j++) pacificStarts.push([0, j]); // 첫 번째 행 (중복 제거)

  // 대서양 시작점들
  const atlanticStarts = [];
  for (let i = 0; i < m; i++) atlanticStarts.push([i, n - 1]); // 마지막 열
  for (let j = 0; j < n - 1; j++) atlanticStarts.push([m - 1, j]); // 마지막 행 (중복 제거)

  // 각 바다에서 DFS 실행
  dfs(pacificStarts, 1); // 태평양: 비트 1
  dfs(atlanticStarts, 2); // 대서양: 비트 2

  return result;
};
