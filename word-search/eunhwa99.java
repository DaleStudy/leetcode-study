class Solution {

  // 시간 복잡도: O(m * n * 4^L) - m: 행, n: 열, L: 단어 길이
  // 공간 복잡도: O(m * n) - 방문 체크를 위한 공간
  public boolean exist(char[][] board, String word) {
    int rows = board.length;
    int cols = board[0].length;

    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        if (dfs(board, word, 0, r, c)) {
          return true;
        }
      }
    }

    return false;
  }

  private boolean dfs(char[][] board, String word, int index, int r, int c) {
    if (index == word.length()) {
      return true;
    }

    if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(
        index)) {
      return false;
    }

    char temp = board[r][c];
    board[r][c] = '#';

    boolean found =
        dfs(board, word, index + 1, r + 1, c) ||
            dfs(board, word, index + 1, r - 1, c) ||
            dfs(board, word, index + 1, r, c + 1) ||
            dfs(board, word, index + 1, r, c - 1);

    board[r][c] = temp;
    return found;
  }
}

