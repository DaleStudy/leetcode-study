/**
 * https://leetcode.com/problems/number-of-islands
 * T.C. O(m*n)
 * S.C. O(m*n)
 */
// function numIslands(grid: string[][]): number {
//   let count = 0;
//   let dir = [[1, 0], [0, 1], [-1, 0], [0, -1]];

//   function removeIsland(r: number, c: number) {
//     if (r < 0 || r >= grid.length) return;
//     if (c < 0 || c >= grid[0].length) return;
//     if (grid[r][c] === '0') return;

//     grid[r][c] = '0';
//     for (let [dr, dc] of dir) {
//       removeIsland(r + dr, c + dc);
//     }
//     return 1;
//   }

//   for (let r = 0; r < grid.length; r++) {
//     for (let c = 0; c < grid[0].length; c++) {
//       if (grid[r][c] === '0') continue;
//       count++;
//       removeIsland(r, c);
//     }
//   }

//   return count;
// }

/**
 * T.C. O(m*n)
 * S.C. O(m*n)
 */
function numIslands(grid: string[][]): number {
  let count = 0;
  let dir = [[1, 0], [0, 1], [-1, 0], [0, -1]];

  function removeIsland(r: number, c: number) {
    const stack = [[r, c]];

    while (stack.length) {
      const [r, c] = stack.pop()!;
      if (r < 0 || r >= grid.length) continue;
      if (c < 0 || c >= grid[0].length) continue;
      if (grid[r][c] === '0') continue;

      grid[r][c] = '0';
      for (let [dr, dc] of dir) {
        stack.push([r + dr, c + dc]);
      }
    }
  }

  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      if (grid[r][c] === '0') continue;
      count++;
      removeIsland(r, c);
    }
  }

  return count;
}
