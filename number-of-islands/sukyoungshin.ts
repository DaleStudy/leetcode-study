function numIslands(grid: string[][]): number {
  let count = 0;

  for (let row = 0; row < grid.length; row++) {
    for (let col = 0; col < grid[0].length; col++) {
      if (grid[row][col] === "1") {
        count++; // 새로운 섬 발견!
        dfs(row, col); // 연결된 모든 "1"을 0으로 바꾸기
      }
    }
  }

  function dfs(row: number, col: number) {
    // 1. 범위를 벗어나거나 이미 물(0)이면 return
    if (row < 0 || col < 0 || row >= grid.length || col >= grid[0].length)
      return;
    if (grid[row][col] === "0") return;

    // 2. 현재 좌표를 0으로 바꾸고
    grid[row][col] = "0";

    // 3. 상하좌우로 dfs 재귀 호출
    dfs(row - 1, col); // 위
    dfs(row + 1, col); // 아래
    dfs(row, col - 1); // 왼쪽
    dfs(row, col + 1); // 오른쪽
  }

  return count;
}
