class SolutionWordSearch {

  int[] dx = new int[]{0, 0, -1, 1};
  int[] dy = new int[]{-1, 1, 0, 0};

  public boolean exist(char[][] board, String word) {
    // 상하좌우 방문 여부 체크하면서 DFS 탐색
    // index 기준으로 word와 비교하면서 같을 때만 추가 탐색
    // 시간복잡도: O(M * N * 4^L) > M: board 행, N: board 열, 4: 상하좌우 4방향, L: word의 길이
    // 공간복잡도: O(1) > 별도 메모리 할당하지 않음
    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[0].length; j++) {
        if (dfs(board, i, j, word, 0)) {
          return true;
        }
      }
    }
    return false;
  }

  public boolean dfs(char[][] board, int x, int y, String word, int index) {
    if (index >= word.length()) {
      return true;
    }
    // board 밖이면 return false
    if (x >= board.length || y >= board[0].length || x < 0 || y < 0) {
      return false;
    }
    // 이미 방문했거나 정답 조건에 맞지 않으면 return false
    if (board[x][y] != word.charAt(index)) {
      return false;
    }

    // 현재 위치의 문자를 임시로 변경하여 방문 처리
    char temp = board[x][y];
    board[x][y] = '#';

    index++;
    for (int i = 0; i < 4; i++) {
      if (dfs(board, x + dx[i], y + dy[i], word, index)) {
        return true;
      }
    }

    // 방문 처리를 되돌림
    board[x][y] = temp;

    return false;
  }
}
