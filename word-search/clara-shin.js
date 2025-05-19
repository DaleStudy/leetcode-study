/**
 * 주어진 격자(board)에서 특정 단어(word)가 존재하는지 확인하는 함수
 *
 * 접근 방식:DFS(깊이 우선 탐색) + 백트래킹
 * 시간 복잡도: O(m * n * 4^k) (m: 행, n: 열, k: 단어 길이)
 * 공간 복잡도: O(m * n) (최대 깊이 m*n)
 *
 */

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
  const m = board.length;
  const n = board[0].length;

  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];

  function dfs(row, col, index) {
    if (index === word.length) {
      return true;
    }

    if (row < 0 || row >= m || col < 0 || col >= n || board[row][col] !== word[index]) {
      return false;
    }

    // 현재 셀 방문 표시 (임시로 변경)
    const temp = board[row][col];
    board[row][col] = '#'; // 방문한 셀을 특수 문자로 표시

    // 네 방향 탐색
    for (const [dx, dy] of directions) {
      const newRow = row + dx;
      const newCol = col + dy;

      if (dfs(newRow, newCol, index + 1)) {
        // 단어를 찾았으면 원래 값 롤백 후 true 반환
        board[row][col] = temp;
        return true;
      }
    }

    // 백트래킹(현재 셀의 원래 값 롤백)
    board[row][col] = temp;

    return false;
  }

  // 격자의 모든 셀에서 시작점으로 시도
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === word[0] && dfs(i, j, 0)) {
        return true;
      }
    }
  }

  // 모든 시작점에서 실패하면
  return false;
};
