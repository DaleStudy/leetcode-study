/**
 * @description
 * brainstorming:
 * dfs
 *
 * time complexity: O(n^2 * 4^word.length)
 * space complexity: O(n^2)
 */

var exist = function (board, word) {
  let answer = false;
  const ROW_LENGTH = board.length;
  const COLUMN_LENGTH = board[0].length;
  // O(n^2)
  const visited = Array.from({ length: ROW_LENGTH }, () =>
    Array.from({ length: COLUMN_LENGTH }, () => false)
  );

  const isRange = (r, c) =>
    r >= 0 && r < ROW_LENGTH && c >= 0 && c < COLUMN_LENGTH && !visited[r][c];

  const search = (r, c, currentWord) => {
    if (answer) return;
    if (currentWord.length > word.length) return;
    if (!word.includes(currentWord)) return;
    if (currentWord === word) {
      answer = true;
      return;
    }

    const dr = [-1, 0, 0, 1];
    const dc = [0, -1, 1, 0];

    for (let i = 0; i < 4; i++) {
      const nextR = r + dr[i];
      const nextC = c + dc[i];

      if (!isRange(nextR, nextC)) continue;

      const nextWord = currentWord + board[nextR][nextC];

      visited[nextR][nextC] = true;
      search(nextR, nextC, nextWord);
      visited[nextR][nextC] = false;
    }
  };

  for (let r = 0; r < ROW_LENGTH; r++) {
    for (let c = 0; c < COLUMN_LENGTH; c++) {
      visited[r][c] = true;
      search(r, c, board[r][c]);
      visited[r][c] = false;
    }
  }

  return answer;
};
