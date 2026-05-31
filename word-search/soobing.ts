function exist(board: string[][], word: string): boolean {
  const move = [[1, 0], [-1, 0], [0, 1], [0, -1]];

  function dfs(row: number, col: number, index: number) {
      if(board[row][col] !== word[index]) return false;
      
      const temp = board[row][col];
      board[row][col] = '#';

      if(index === word.length - 1) return true;
      for(const [dx, dy] of move) {
          if(row + dx < 0 || row + dx >= board.length) continue;
          if(col + dy < 0 || col + dy >= board[0].length) continue;
          if(dfs(row + dx, col + dy, index + 1)) return true;
      }

      board[row][col] = temp;
  }

  for (let r = 0; r < board.length; r++) {
    for (let c = 0; c < board[0].length; c++) {
        if (dfs(r, c, 0)) return true;
    }
}
  return false;
};
