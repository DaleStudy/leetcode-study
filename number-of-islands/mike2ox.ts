/**
 * https://leetcode.com/problems/number-of-islands/
 * 풀이방법: BFS를 사용하여 섬의 개수를 구함
 *
 * 시간복잡도: O(n * m) (n: 그리드의 행, m: 그리드의 열)
 * 공간복잡도: O(n * m) (그리드의 모든 요소를 방문)
 */

function numIslands(grid: string[][]): number {
  if (!grid.length) return 0; // 그리드가 비어있는 경우

  const rows = grid.length;
  const cols = grid[0].length;
  let islands = 0;

  const bfs = (startRow: number, startCol: number) => {
    const q: number[][] = [[startRow, startCol]];
    grid[startRow][startCol] = "0";

    const directions = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ]; // 상하좌우

    while (q.length) {
      const [r, c] = q.shift()!;

      for (const [dx, dy] of directions) {
        const newR = r + dx;
        const newC = c + dy;

        if (
          newR >= 0 &&
          newR < rows &&
          newC >= 0 &&
          newC < cols &&
          grid[newR][newC] === "1"
        ) {
          q.push([newR, newC]);
          grid[newR][newC] = "0";
        }
      }
    }
  };

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] === "1") {
        islands++;
        bfs(r, c);
      }
    }
  }

  return islands;
}
