import java.util.LinkedList;
import java.util.Queue;

// BFS 사용
// 시간 복잡도 : O(MxN)
// 공간 복잡도: O(MxN)
class Solution {

  int[][] dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

  public int numIslands(char[][] grid) {
    int row = grid.length;
    int col = grid[0].length;

    int total = 0;
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        if (grid[i][j] == '1') {
          total++;
          BFS(grid, i, j, row, col);
          System.out.println(grid[i][j]);
        }
      }
    }
    return total;
  }

  private void BFS(char[][] grid, int r, int c, int sizeR, int sizeC) {
    Queue<Position> queue = new LinkedList<>();

    queue.add(new Position(r, c));
    grid[r][c] = '0'; // '0'으로 변경 (방문 체크)

    while (!queue.isEmpty()) {
      Position current = queue.poll();
      int curR = current.r;
      int curC = current.c;

      for (int i = 0; i < 4; i++) {
        int dirR = dir[i][0];
        int dirC = dir[i][1];

        int nextR = curR + dirR;
        int nextC = curC + dirC;

        if (nextR < 0 || nextR >= sizeR || nextC < 0 || nextC >= sizeC || grid[nextR][nextC] == '0') {
          continue;
        }
        queue.add(new Position(nextR, nextC));
        grid[nextR][nextC] = '0';
      }
    }

  }

  static class Position {

    int r;
    int c;

    Position(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }
}
