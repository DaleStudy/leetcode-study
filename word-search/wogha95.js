// 2차
// result flag 변수를 활용 => boolean 반환으로 개선
// TC: O(M * N * 4^W)
// SC: O(MIN)
// W: word.length, MIN: min(M * N, W)

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  for (let r = 0; r < board.length; r++) {
    for (let c = 0; c < board[0].length; c++) {
      if (dfs(r, c, 0)) {
        return true;
      }
    }
  }

  return false;

  function dfs(row, column, wordIndex) {
    if (!isValid(row, column)) {
      return false;
    }
    if (board[row][column] !== word[wordIndex]) {
      return false;
    }
    if (wordIndex === word.length - 1) {
      return true;
    }

    const temp = board[row][column];
    board[row][column] = "#";

    if (
      dfs(row + 1, column, wordIndex + 1) ||
      dfs(row - 1, column, wordIndex + 1) ||
      dfs(row, column + 1, wordIndex + 1) ||
      dfs(row, column - 1, wordIndex + 1)
    ) {
      return true;
    }

    board[row][column] = temp;

    return false;
  }

  function isValid(row, column) {
    if (row < 0 || board.length <= row) {
      return false;
    }
    if (column < 0 || board[0].length <= column) {
      return false;
    }
    return true;
  }
};

// 1차
// TC: O(M * N * 4^W)
// SC: O(MIN)
// W: word.length, MIN: min(M * N, W)

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  let result = false;

  // 1. 2차원 배열의 모든 좌표를 순회
  for (let r = 0; r < board.length; r++) {
    for (let c = 0; c < board[0].length; c++) {
      dfs(r, c, 0);
    }
  }

  return result;

  function dfs(row, column, wordIndex) {
    // 2. 범위를 벗어난 좌표인지 검증
    if (!isValid(row, column)) {
      return;
    }
    // 3. word에서 찾고 있는 문자인지 확인
    if (board[row][column] !== word[wordIndex]) {
      return;
    }
    // 4. word 문자를 다 찾았는지 확인
    if (wordIndex === word.length - 1) {
      result = true;
      return;
    }

    // 5. 방문한 좌표를 표시하기 위해 다른 문자로 바꿔치기 해둠
    const temp = board[row][column];
    board[row][column] = "#";
    // 6. 상하좌우로 좌표 방문
    dfs(row + 1, column, wordIndex + 1);
    dfs(row - 1, column, wordIndex + 1);
    dfs(row, column + 1, wordIndex + 1);
    dfs(row, column - 1, wordIndex + 1);
    // 7. 해당 좌표의 재귀 방문이 끝나면 미방문으로 표시하기 위해 원래 문자로 되돌리기
    board[row][column] = temp;
  }

  // 유효한 좌표인지 확인하는 함수
  function isValid(row, column) {
    if (row < 0 || board.length <= row) {
      return false;
    }
    if (column < 0 || board[0].length <= column) {
      return false;
    }
    return true;
  }
};
