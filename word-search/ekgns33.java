/*
input : m x n matrix and string word
output : return true if given word can be constructed

solution 1) brute force
tc : O(n * 4^k) when n is the number of cells, k is the length of word
sc : O(k) call stack
 */
class Solution {
  private int[][] directions = new int[][] {{-1,0}, {1,0}, {0,1}, {0,-1}};
  public boolean exist(char[][] board, String word) {
    //edge case
    int m = board.length;
    int n = board[0].length;

    if(m * n < word.length()) return false;


    //look for the starting letter and do dfs
    for(int i = 0; i < m; i++) {

      for(int j = 0; j < n; j++) {

        if(board[i][j] == word.charAt(0)) {
          //do dfs and get answer
          board[i][j] = '0';
          boolean res = dfsHelper(board, word, i, j, 1);
          board[i][j] = word.charAt(0);
          if(res) return true;
        }
      }
    }

    return false;
  }

  public boolean dfsHelper(char[][] board, String word, int curR, int curC, int curP) {

    //endclause
    if(curP == word.length()) return true;

    boolean ret = false;

    for(int[] direction : directions) {
      int nextR = curR + direction[0];
      int nextC = curC + direction[1];

      if(nextR < 0 || nextR >= board.length || nextC < 0 || nextC >= board[0].length) continue;

      if(board[nextR][nextC] == word.charAt(curP)) {
        board[nextR][nextC] = '0';
        ret = ret || dfsHelper(board, word, nextR, nextC, curP + 1);
        board[nextR][nextC] = word.charAt(curP);
      }
    }
    return ret;
  }
}
