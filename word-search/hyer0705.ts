function exist(board: string[][], word: string): boolean {
  const m = board.length;
  const n = board[0].length;

  const visited: boolean[][] = Array.from({ length: m }, () => Array(n).fill(false));

  const isValidCoordinates = (index: number, x: number, y: number): boolean => {
    if (x >= 0 && x < m && y >= 0 && y < n && word[index] === board[x][y] && !visited[x][y]) return true;
    return false;
  };

  const backtrack = (index: number, cx: number, cy: number): boolean => {
    if (index === word.length - 1 && board[cx][cy] === word[index]) return true;

    if (board[cx][cy] !== word[index]) return false;

    for (const [dx, dy] of [
      [0, 1],
      [0, -1],
      [1, 0],
      [-1, 0],
    ]) {
      const [nx, ny] = [cx + dx, cy + dy];

      if (isValidCoordinates(index + 1, nx, ny)) {
        visited[nx][ny] = true;
        const result = backtrack(index + 1, nx, ny);
        if (result) return true;
        visited[nx][ny] = false;
      }
    }

    return false;
  };

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === word[0]) {
        visited[i][j] = true;
        const result: boolean = backtrack(0, i, j);
        if (result) return true;
        visited[i][j] = false;
      }
    }
  }

  return false;
}
