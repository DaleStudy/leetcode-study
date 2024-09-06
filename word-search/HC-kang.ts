/**
 * https://leetcode.com/problems/word-search
 * T.C. O(n * m * 4^l)
 * S.C. O(n * m)
 */
function exist(board: string[][], word: string): boolean {
  const countMap = new Map<string, number>();

  for (let i = 0; i < word.length; i++) {
    countMap.set(word[i], (countMap.get(word[i]) || 0) + 1);
  }
  for (let i = 0; i < board.length * board[0].length; i++) {
    countMap.set(board[Math.floor(i / board[0].length)][i % board[0].length], 0);
  }

  if (Array.from(countMap.values()).some((v) => v > 0)) return false;

  let seen = Array.from({ length: board.length }, () =>
    new Array(board[0].length).fill(false)
  );
  const directives = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  function dfs(h: number, w: number, index: number): boolean {
    if (w < 0 || w >= board[0].length) return false;
    if (h < 0 || h >= board.length) return false;

    if (seen[h][w]) return false;
    if (board[h][w] !== word[index]) return false;
    if (index === word.length - 1) return true;

    seen[h][w] = true;

    for (let i = 0; i < 4; i++) {
      const [dh, dw] = directives[i];
      if (dfs(h + dh, w + dw, index + 1)) {
        return true;
      }
    }

    seen[h][w] = false;
    return false;
  }

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (dfs(i, j, 0)) {
        return true;
      }
    }
  }
  return false;
}
