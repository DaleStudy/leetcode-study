// sc : O(n*m)
// tc : O(n*m)
function numIslands(grid: string[][]): number {
  let count = 0;
  const visited = Array.from({length: grid.length}, () =>
    Array.from({length: grid[0].length}, () => false),
  );
  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  function explore(x, y) {
    visited[x][y] = true;
    for (let [dx, dy] of directions) {
      const nx = dx + x;
      const ny = dy + y;
      if (
        nx < grid.length &&
        ny < grid[0].length &&
        nx >= 0 &&
        ny >= 0 &&
        !visited[nx][ny] &&
        grid[nx][ny] === '1'
      ) {
        explore(nx, ny);
      }
    }
  }

  for (let x = 0; x < grid.length; x++) {
    for (let y = 0; y < grid[x].length; y++) {
      if (!visited[x][y] && grid[x][y] === '1') {
        count++;
        explore(x, y);
      }
    }
  }
  return count;
}
