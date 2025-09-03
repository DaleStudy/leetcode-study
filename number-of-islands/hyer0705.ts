function numIslands(grid: string[][]): number {
  const m = grid.length;
  const n = grid[0].length;

  const LAND = "1";
  const WATER = "0";

  const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));

  const isValid = (row: number, col: number): boolean => row >= 0 && row < m && col >= 0 && col < n;

  const bfs = (row: number, col: number): void => {
    const directions = [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ];

    // [row, col][]
    const queue: number[][] = [];

    visited[row][col] = true;
    queue.push([row, col]);

    while (queue.length > 0) {
      const [cx, cy] = queue.shift()!;

      for (const [dx, dy] of directions) {
        const [nx, ny] = [cx + dx, cy + dy];

        if (isValid(nx, ny) && !visited[nx][ny] && grid[nx][ny] === LAND) {
          visited[nx][ny] = true;
          queue.push([nx, ny]);
        }
      }
    }
  };

  let island = 0;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === LAND && !visited[i][j]) {
        island++;
        bfs(i, j);
      }
    }
  }

  return island;
}
