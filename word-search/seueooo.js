/**
현재 경로를 하나 선택해서 끝까지 진행하고, 실패하면 방문 표시를 되돌려 다른 경로를 시도
bfs, 백트래킹
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  const rows = board.length;
  const cols = board[0].length;

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  function dfs(x, y, index) {
    if (board[y][x] !== word[index]) {
      return false;
    }

    if (index === word.length - 1) {
      return true;
    }

    // 방문 처리
    const original = board[y][x];
    board[y][x] = "#";

    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (
        nx >= 0 &&
        nx < cols &&
        ny >= 0 &&
        ny < rows &&
        board[ny][nx] !== "#"
      ) {
        if (dfs(nx, ny, index + 1)) {
          board[y][x] = original;
          return true;
        }
      }
    }

    board[y][x] = original;
    return false;
  }

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (dfs(j, i, 0)) return true;
    }
  }
  return false;
};
