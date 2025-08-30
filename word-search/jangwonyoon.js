/**
 * 79. Word Search
 * https://leetcode.com/problems/word-search/
 *
 */

/*
 * 시간 복잡도(TC): O(m * n * 4^L)
 * m = 행, n = 열, L = 단어 길이
 *
 * 공간 복잡도(SC): O(L)
 * L = 단어 길이
 *
 * 관련 알고리즘: 깊이 우선 탐색 Depth-First Search (DFS)
 *
 * 문제 풀이 방법:
 * 1. 깊이 우선 탐색 (DFS)을 사용하여 시작점부터 첫 글자가 맞는 칸에서만 탐색
 * 2. 탐색 결과를 반환
 */
/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const rows = board.length;
    const cols = board[0].length;

    function dfs(r, c, idx) {
        // 1) 기저: 단어를 모두 매칭했을 경우 - 탈출 조건
        if (idx === word.length) return true;

        // 2) 가드: 범위/문자/방문 상태 확인
        if (r < 0 || r >= rows || c < 0 || c >= cols) return false;
        if (board[r][c] !== word[idx]) return false;
        if (board[r][c] === '#') return false; // 이미 방문했으면 탈락

        // 3) 방문 마킹
        const tmp = board[r][c];
        board[r][c] = '#';

        // 4방향 탐색 (상, 하, 좌, 우)
        const ok = ㅋ
            dfs(r + 1, c, idx + 1) ||
            dfs(r - 1, c, idx + 1) ||
            dfs(r, c + 1, idx + 1) ||
            dfs(r, c - 1, idx + 1);

        // 5) 복구
        board[r][c] = tmp;

        return ok;
    }

    // 시작점: 첫 글자와 일치하는 칸에서만 DFS 시작
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            // 첫 글자가 맞으면서 dfs가 성공했을 경우 true 반환
            if (board[row][col] === word[0] && dfs(row, col, 0)) return true;
        }
    }

    return false;
};

/**
 * 풀이 2
 * 방문 배열 사용
 *
 * 시간 복잡도(TC): O(m * n * 4^L)
 * 공간 복잡도(SC): O(m * n)
 *
 * 관련 알고리즘: 깊이 우선 탐색 Depth-First Search (DFS)
 *
 * 문제 풀이 방법:
 * 1. 방문 배열을 사용하여 방문한 칸을 체크

 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */

var exist = function(board, word) {
  const rows = board.length;
  const cols = board[0].length;

  // visited 배열 초기화
  const visited = Array.from({ length: rows }, () => Array(cols).fill(false));

  function dfs(r, c, idx) {
    // 1) 기저 조건: 단어를 모두 찾은 경우
    if (idx === word.length) return true;

    // 2) 가드 조건
    if (r < 0 || r >= rows || c < 0 || c >= cols) return false;
    if (visited[r][c]) return false;
    if (board[r][c] !== word[idx]) return false;

    // 3) 방문 처리
    visited[r][c] = true;

    // 4) 네 방향 탐색
    const ok =
      dfs(r + 1, c, idx + 1) ||
      dfs(r - 1, c, idx + 1) ||
      dfs(r, c + 1, idx + 1) ||
      dfs(r, c - 1, idx + 1);

    // 5) 복구 (다른 경로에서 다시 쓸 수 있게)
    visited[r][c] = false;

    return ok;
  }

  // 6) 시작점 순회
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (board[r][c] === word[0] && dfs(r, c, 0)) return true;
    }
  }

  return false;
};
