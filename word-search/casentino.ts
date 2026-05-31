function exist(board: string[][], word: string): boolean {
  const m = board.length;
  const n = board[0].length;

  const visited = Array.from({ length: m }, () => new Array(n).fill(0));
  function findDirection(currentI: number, currentJ: number, findNextIdx: number) {
    if (findNextIdx === word.length) {
      return true;
    }
    if (
      currentI < 0 ||
      currentJ < 0 ||
      currentI >= m ||
      currentJ >= n ||
      board[currentI][currentJ] !== word[findNextIdx]
    ) {
      return false;
    }
    if (visited[currentI][currentJ] === 1) {
      return false;
    }
    visited[currentI][currentJ] = 1;

    const isApproachLastWord =
      findDirection(currentI + 1, currentJ, findNextIdx + 1) ||
      findDirection(currentI - 1, currentJ, findNextIdx + 1) ||
      findDirection(currentI, currentJ - 1, findNextIdx + 1) ||
      findDirection(currentI, currentJ + 1, findNextIdx + 1);

    if (!isApproachLastWord) {
      visited[currentI][currentJ] = 0;
    }
    return isApproachLastWord;
  }
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      const result = findDirection(i, j, 0);
      if (result) {
        return true;
      }
    }
  }
  return false;
}
