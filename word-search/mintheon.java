class Solution {
  // BFS로 변환해서 다시 풀어볼 것
  char[][] board;
  boolean[][] visited;
  int[] moveX = {-1, 1, 0, 0};
  int[] moveY = {0, 0, -1, 1};
  int row, col;

  public boolean exist(char[][] board, String word) {
    this.board = board;
    this.row = board.length;
    this.col = board[0].length;
    this.visited = new boolean[row][col];

    for(int y = 0; y < row; y++) {
      for(int x = 0; x < col; x++) {
        if(this.hasWord(y, x, word, 0)) {
          return true;
        }
      }
    }

    return false;
  }

  private boolean hasWord(int y, int x, String word, int index) {
    if(index >= word.length()) {
      return true;
    }

    if(x < 0 || x >= col || y < 0 || y >= row || visited[y][x] || board[y][x] != word.charAt(index)) {
      return false;
    }

    this.visited[y][x] = true;
    for(int i = 0; i < 4; i++) {
      if(this.hasWord(y + moveY[i], x + moveX[i], word, index + 1)) {
        return true;
      }
    }

    this.visited[y][x] = false;
    return false;
  }
}
