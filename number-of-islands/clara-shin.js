/**
 * 섬의 개수 찾기 - 그래프 탐색 문제
 * 2차원 바이너리 그리드, 1은 섬, 0은 물
 * 그리드의 모든 가장자리는 물로 둘러싸여 있음
 *
 * 문제 접근: BFS(너비 우선 탐색) 사용
 * 1. 그리드를 순회하면서 땅(1)을 발견하면 BFS로 연결된 모든 땅을 탐색
 * 2. BFS 탐색 중에 방문한 땅은 방문 배열에 표시
 * 3. BFS 탐색이 끝나면 섬의 개수를 증가
 * 4. 그리드 전체를 순회하면서 섬의 개수를 세기
 *
 * BFS 선택 이유: 제약 조건(그리드 크기 최대 300x300)을 고려했을 때,
 * - 그리드가 커질수록 DFS는 재귀 호출로 인한 스택 오버플로우 위험이 있음,
 * - BFS는 큐를 사용하여 이 위험을 피할 수 있음
 * - 방문배열을 만들어서 원본데이터 보존(불변성 유지)
 * - 단, BFS는 큐를 사용하므로 메모리 사용량이 더 많을 수 있음
 *
 * 시간 복잡도: O(M×N) (M: 행의 개수, N: 열의 개수)
 * 공간 복잡도: O(M×N) (방문 배열과 큐를 사용)
 */
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  if (!grid || grid.length === 0) {
    return 0;
  }

  const rows = grid.length;
  const cols = grid[0].length;
  let islandCount = 0;

  // 방문 배열 생성
  const visited = Array(rows)
    .fill()
    .map(() => Array(cols).fill(false));

  // 방향 배열 (상, 하, 좌, 우)
  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  function bfs(startRow, startCol) {
    const queue = [[startRow, startCol]];
    visited[startRow][startCol] = true; // 시작점 방문 처리

    while (queue.length > 0) {
      const [row, col] = queue.shift();

      // 4방향 탐색
      for (const [dr, dc] of directions) {
        const newRow = row + dr;
        const newCol = col + dc;

        // 범위 안에서, 방문하지 않은 땅('1')이면 탐색
        if (
          newRow >= 0 &&
          newRow < rows &&
          newCol >= 0 &&
          newCol < cols &&
          grid[newRow][newCol] === '1' &&
          !visited[newRow][newCol]
        ) {
          queue.push([newRow, newCol]);
          visited[newRow][newCol] = true; // 방문 처리
        }
      }
    }
  }

  // 그리드 전체 순회
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      // 땅('1')을 발견하고 아직 방문하지 않았으면 BFS 시작 및 섬 카운트 증가
      if (grid[i][j] === '1' && !visited[i][j]) {
        islandCount++;
        bfs(i, j);
      }
    }
  }

  return islandCount;
};
