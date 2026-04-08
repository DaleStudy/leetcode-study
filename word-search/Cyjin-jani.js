//! dfs 구현 중에 막혀서 ai의 도움을 받아 풀이를 완성했습니다..
var exist = function (board, word) {
  const dx = [0, 0, -1, 1];
  const dy = [-1, 1, 0, 0];

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === word[0]) {
        if (dfs(j, i, 0)) return true;
      }
    }
  }

  function dfs(x, y, index) {
    // 성공
    if (index === word.length) return true;

    // 실패
    if (x < 0 || y < 0 || y >= board.length || x >= board[y].length) return false;
    if (board[y][x] === '#') return false;
    if (board[y][x] !== word[index]) return false;

    // 방문 표시
    const origin = board[y][x];
    board[y][x] = '#';

    // 탐색
    for (let i = 0; i < 4; i++) {
      const newDy = y + dy[i];
      const newDx = x + dx[i];

      if (dfs(newDx, newDy, index + 1)) return true;
    }
    // 복원
    board[y][x] = origin;

    return false;
  }

  return false;
};
