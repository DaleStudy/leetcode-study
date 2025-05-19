/**
 * 문제 설명
 * - 2차원 그리드에서 섬의 갯수를 구하는 문제
 *
 * 조건
 * - 가로, 세로가 1로 인접해있는 경우 같은 섬으로 간주
 *
 * 아이디어
 * - 경로 탐색, 네트워크, 조합 유형이 나오면 '그래프 탐색 알고리즘'을 떠울린다.
 * 1) DFS (재귀)
 * 2) BFS (링크드리스트 or 큐)
 *
 */

function numIslands(grid: string[][]): number {
  const rows = grid.length;
  const cols = grid[0].length;
  let count = 0;
  function dfs(r: number, c: number) {
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] === "0") return;

    grid[r][c] = "0";
    dfs(r - 1, c);
    dfs(r + 1, c);
    dfs(r, c - 1);
    dfs(r, c + 1);
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === "1") {
        count++;
        dfs(r, c);
      }
    }
  }
  return count;
}

/**
 * 
 * BFS version

function numIslands(grid: string[][]): number {
  const rows = grid.length;
  const cols = grid[0].length;
  let count = 0;

  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  function bfs(r: number, c: number) {
    const queue = [[r, c]];
    grid[r][c] = "0";

    while (queue.length) {
      const [row, col] = queue.shift()!;

      for (const [dr, dc] of directions) {
        const newRow = row + dr;
        const newCol = col + dc;

        if (
          newRow >= 0 &&
          newRow < rows &&
          newCol >= 0 &&
          newCol < cols &&
          grid[newRow][newCol] === "1"
        ) {
          queue.push([newRow, newCol]);
          grid[newRow][newCol] = "0";
        }
      }
    }
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === "1") {
        count++;
        bfs(r, c);
      }
    }
  }
  return count;
}

 */
