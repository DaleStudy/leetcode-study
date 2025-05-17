/**
 * https://leetcode.com/problems/number-of-islands/
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  if (!grid || grid.length === 0) return 0;

  const rows = grid.length;
  const cols = grid[0].length;
  let count = 0;

  const dfs = (r, c) => {
    // 경계 밖이거나 물인 경우 리턴
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] === "0") {
      return;
    }

    // 방문 표시 (육지를 물로 바꿈)
    grid[r][c] = "0";

    // 상하좌우 탐색
    dfs(r - 1, c); // 위
    dfs(r + 1, c); // 아래
    dfs(r, c - 1); // 왼쪽
    dfs(r, c + 1); // 오른쪽
  };

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === "1") {
        count++;
        dfs(r, c); // 해당 섬 전체 방문 처리
      }
    }
  }

  return count;
};
