/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
// DFS 사용 이유: 한 경로를 끝까지 탐색해야 하고, 경로별로 독립적인 방문 상태가 필요하기 때문
// BFS 불가 이유: 여러 경로를 동시에 탐색하면서 방문 상태가 섞여 올바른 경로를 놓칠 수 있음
var exist = function (board, word) {
  for (let y = 0; y < board.length; y++) {
    for (let x = 0; x < board[0].length; x++) {
      // 시작이 되는 단어를 마주치면 dfs 돌려보기
      if (board[y][x] === word[0] && dfs(board, y, x, word, 0)) {
        return true;
      }
    }
  }
  return false;
};

function dfs(board, y, x, word, index) {
  // 성공 조건: 모든 문자를 찾았을 때
  if (index === word.length) return true;

  // 실패 조건: 범위를 벗어나거나 현재 글자가 일치하지 않을 때
  if (
    y < 0 ||
    y >= board.length ||
    x < 0 ||
    x >= board[0].length ||
    board[y][x] !== word[index]
  ) {
    return false;
  }

  // 현재 셀 사용 표시
  const temp = board[y][x];
  board[y][x] = true; // 임시 방문 표시

  // 상하좌우 탐색, 하나라도 찾게된다면 true
  const found =
    dfs(board, y + 1, x, word, index + 1) ||
    dfs(board, y - 1, x, word, index + 1) ||
    dfs(board, y, x + 1, word, index + 1) ||
    dfs(board, y, x - 1, word, index + 1);

  // 원래 값으로 복원 (백트래킹)
  board[y][x] = temp;

  return found;
}
