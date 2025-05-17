/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  const rows = board.length;
  const cols = board[0].length;

  function backtrack(row, col, index) {
    // 종료 조건: 모든 글자를 찾았으면 true
    if (index === word.length) return true;

    // 범위 밖이거나, 현재 칸 글자가 다르면 false
    if (
      row < 0 ||
      row >= rows ||
      col < 0 ||
      col >= cols ||
      board[row][col] !== word[index]
    ) {
      return false;
    }

    // 방문 처리 (임시로 다른 문자로 바꿔줌)
    const temp = board[row][col];
    board[row][col] = "#";

    // 상하좌우로 이동하면서 다음 글자 찾기
    const found =
      backtrack(row + 1, col, index + 1) || // 아래
      backtrack(row - 1, col, index + 1) || // 위
      backtrack(row, col + 1, index + 1) || // 오른쪽
      backtrack(row, col - 1, index + 1); // 왼쪽

    // 복구 (다시 원래 문자로 되돌리기)
    board[row][col] = temp;

    return found;
  }

  // board 전체 돌면서 시작점 찾기
  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (backtrack(row, col, 0)) {
        return true;
      }
    }
  }

  return false;
};
