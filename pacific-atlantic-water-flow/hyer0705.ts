function pacificAtlantic(heights: number[][]): number[][] {
  const m = heights.length;
  const n = heights[0].length;

  const directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  const helper = (row: number, col: number): boolean[][] => {
    const canReach: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));

    const queue: [number, number][] = [];

    for (let i = 0; i < n; i++) {
      canReach[row][i] = true;
      queue.push([row, i]);
    }
    for (let i = 0; i < m; i++) {
      canReach[i][col] = true;
      queue.push([i, col]);
    }

    while (queue.length > 0) {
      const [cx, cy] = queue.shift()!;

      for (const [dx, dy] of directions) {
        const [nx, ny] = [cx + dx, cy + dy];

        if (nx >= 0 && nx < m && ny >= 0 && ny < n && !canReach[nx][ny] && heights[cx][cy] <= heights[nx][ny]) {
          canReach[nx][ny] = true;
          queue.push([nx, ny]);
        }
      }
    }

    return canReach;
  };

  const canReachPacific: boolean[][] = helper(0, 0);
  const canReachAtlantic: boolean[][] = helper(m - 1, n - 1);

  const results: number[][] = [];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (canReachPacific[i][j] && canReachAtlantic[i][j]) results.push([i, j]);
    }
  }

  return results;
}
