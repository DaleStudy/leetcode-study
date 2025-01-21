/**
 input : 2d matrix filled with '1', '0'
 output : number of islands

 1 indicates land, 0 means water.
 if lands are surrounded by water we call it island

 example

 1 1 1.  >> 3 islands
 0 0 0
 1 0 1

 1 1 1 1 0
 1 1 0 1 0 >> 1 island
 0 0 0 0 0

 constraints:
 1) m, n range
 [1, 300]
 2) can we change the input grid cell?
 there is no restriction.

 solution 1)

 ds : array
 algo : bfs + in-place

 read every cell in grid.
 if cell is '1'
 do bfs, change every visiting cell into '2' << if changing input is allowed.
 increase count

 tc : O(mn), visiting each cell exactly once.
 sc : O(mn) for queue

 optimize?? maintain visited matrix, set or something else..
 if we are allowed to modify given input matrix
 we don't have to maintain visited matrix, but simply change values
 */
class Solution {
  public int numIslands(char[][] grid) {
    int m = grid.length, n = grid[0].length;
    int numberOfIslands = 0;
    for(int i = 0; i < m; i++) {
      for(int j = 0; j < n; j++) {
        if(grid[i][j] == '1') {
          bfsHelper(grid, i, j, m, n);
          numberOfIslands++;
        }
      }
    }
    return numberOfIslands;
  }
  private static int[][] directions = {
      {1, 0}, {-1, 0}, {0, 1}, {0, -1}
  };

  private void bfsHelper(char[][] grid, int x, int y, int m, int n) {
    Queue<int[]> queue = new LinkedList<>();
    queue.add(new int[]{x,y});
    grid[x][y] = '2';
    while(!queue.isEmpty()) {
      int[] cur = queue.poll();
      for(int[] direction : directions) {
        int nx = direction[0] + cur[0];
        int ny = direction[1] + cur[1];
        if(nx < 0 || nx >= m || ny < 0 || ny >= n || grid[nx][ny] != '1') continue;
        grid[nx][ny] = '2';
        queue.add(new int[]{nx, ny});
      }
    }
  }
}
