/*
* input : grid represents the heights of island
* output : coordinates where water flows to both pacific and atlantic
*
* example
*
*  2 2 2   1,1 >> 1,2 >> atlantic / 1,1 >> 0,1 >> pacific
*  3 3 1
*  4 3 1
*
* do dfs/bfs from the edge of grids.
* if cell is checked from pacific and atlantic add to result
* solution  dfs from edges
*   tc : O(m*n)
*   sc : O(mn)
*
* */
class Solution {
  public List<List<Integer>> pacificAtlantic(int[][] heights) {
    int m = heights.length;
    int n = heights[0].length;
    int[][] pacific = new int[m][n];
    int[][] atlantic = new int[m][n];

    for(int i = 0; i < m; i++) {
      dfsHelper(heights, pacific, i, 0);
    }
    for(int j = 1; j < n; j++) {
      dfsHelper(heights,pacific, 0, j);
    }
    for(int i =0; i < m; i++) {
      dfsHelper(heights,atlantic, i, n-1);
    }
    for(int j = 0; j < n-1; j++) {
      dfsHelper(heights, atlantic, m-1, j);
    }
    List<List<Integer>> ans = new ArrayList<>();
    for(int i = 0; i < m; i++) {
      for(int j = 0; j < n; j++) {
        if(pacific[i][j] == 1 && atlantic[i][j] == 1) {
          ans.add(List.of(i, j));
        }
      }
    }
    return ans;
  }

  static int[][] directions = {
      {1, 0}, {-1, 0}, {0, 1}, {0, -1}
  };

  void dfsHelper(int[][] board, int[][] visited, int x, int y) {
    if(visited[x][y] > 0) return;
    visited[x][y] += 1;
    for(int[] direction : directions) {
      int nx = x + direction[0];
      int ny = y + direction[1];
      if(nx < 0 || nx >=visited.length || ny < 0 || ny >= visited[0].length || visited[nx][ny] > 0 || board[nx][ny] < board[x][y]) continue;
      dfsHelper(board, visited, nx, ny);
    }
  }
}
