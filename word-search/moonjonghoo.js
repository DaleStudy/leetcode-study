/**
 * 🔢 문제 이름: Word Search (LeetCode 79)
 * 🧩 문제 유형: DFS + Backtracking
 *
 * 🎯 문제 설명:
 * 주어진 2차원 문자 격자(board)와 문자열(word)에서,
 * 단어가 board 안에서 인접한 셀(상하좌우)을 통해 존재하는지를 판별하라.
 * 각 셀은 한 번만 사용할 수 있으며, 대각선 이동은 허용되지 않는다.
 *
 * 💡 핵심 아이디어:
 * - 모든 셀을 시작점으로 삼아 DFS 탐색
 * - 현재 문자가 일치하면 다음 문자로 재귀 호출
 * - visited 배열을 통해 중복 방문을 방지
 * - DFS 중 완성된 경로가 있으면 true 반환
 *
 * 📈 시간복잡도: O(N * 3^L)
 *   - N = 전체 셀 수, L = 단어 길이
 *   - 각 셀마다 최대 3 방향으로 탐색 (이전 셀 제외)
 *
 * 📦 공간복잡도: O(L) — DFS 재귀 깊이 (단어 길이)
 */

function exist(board, word) {
  const rows = board.length;
  const cols = board[0].length;

  // 1. visited 배열 초기화
  const visited = Array.from({ length: rows }, () => Array(cols).fill(false));

  // 2. DFS 함수 정의
  function dfs(x, y, idx) {
    // 모든 문자를 찾았으면 성공
    if (idx === word.length) return true;

    // 범위를 벗어나거나, 이미 방문했거나, 문자 불일치 → 실패
    if (
      x < 0 ||
      x >= rows ||
      y < 0 ||
      y >= cols ||
      visited[x][y] ||
      board[x][y] !== word[idx]
    )
      return false;

    // 현재 위치 방문 처리
    visited[x][y] = true;

    // 상하좌우 방향 정의
    const directions = [
      [1, 0],
      [-1, 0],
      [0, 1],
      [0, -1],
    ];

    // 3. 다음 문자 탐색
    for (let [dx, dy] of directions) {
      if (dfs(x + dx, y + dy, idx + 1)) return true;
    }

    // 4. 백트래킹 (방문 상태 복원)
    visited[x][y] = false;
    return false;
  }

  // 5. 모든 셀에서 DFS 시작 시도
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (board[i][j] === word[0] && dfs(i, j, 0)) {
        return true;
      }
    }
  }

  return false;
}
