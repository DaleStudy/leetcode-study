/**
 *
 * 접근 방법 :
 * 1. 행렬 순회하며 word와 첫 번째 문자가 같은지 체크
 * 2. 같으면 DFS(재귀)로 네 방향(상하좌우)을 탐색한다.
 *    - 현재 위치가 유효한지 체크 = 범위 안인가, 문자가 같은가
 *    - 단어 다 찾아서 index가 단어 길이와 같은지 체크
 * 3. 이미 방문한 노드 제외하기 위해서 네 방향 체크하기 전에 방문 여부 표시하기
 * 4. 4방향으로 문자 체크하기
 * 5. 재귀 호출하는 동안 찾지 못한 경우 방문 여부 초기화하기 (backtracking)
 *
 * 시간복잡도 : O(N * M * 4^L)
 * - L는 word의 길이, word 길이만큼 네 방향 체크하니까 O(4^L)
 * 공간복잡도 : O(L)
 *
 * - L는 word의 길이, 찾으려는 단어 길이만큼 재귀 호출되니까 O(L)
 *
 */

function exist(board: string[][], word: string): boolean {
  const rows = board.length;
  const cols = board[0].length;

  const dfs = (x: number, y: number, index: number): boolean => {
    // 종료조건 : 문자를 다 찾은 경우
    if (index === word.length) return true;

    // 범위를 벗어나거나 이미 방문했거나 문자가 다른 경우
    if (x < 0 || y < 0 || x >= rows || y >= cols || board[x][y] !== word[index])
      return false;

    // 방문 표시
    const temp = board[x][y];
    board[x][y] = "#";

    // 4 방향
    const directions = [
      [1, 0],
      [0, 1],
      [-1, 0],
      [0, -1],
    ];

    for (const [dx, dy] of directions) {
      if (dfs(x + dx, y + dy, index + 1)) return true;
    }

    // 백트래킹
    board[x][y] = temp;
    return false;
  };

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (word[0] === board[i][j] && dfs(i, j, 0)) return true;
    }
  }

  return false;
}
