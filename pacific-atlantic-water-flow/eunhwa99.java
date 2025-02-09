import java.util.ArrayList;
import java.util.List;

class Solution {

  // TP: O(N*N)
  // SP: O(N*N)
  // pacific에 접하는 지점으로부터 dfs를 시작해 pacific에 도달할 수 있는 지점을 체크하고,
  // atlantic에 접하는 지점으로부터 dfs를 시작해 atlantic에 도달할 수 있는 지점을 체크한다.
  // 마지막으로 두 지점 모두에 도달할 수 있는 지점을 찾아 반환한다.
  int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

  public List<List<Integer>> pacificAtlantic(int[][] heights) {
    int rowSize = heights.length;
    int colSize = heights[0].length;

    boolean[][] pacific = new boolean[rowSize][colSize];
    boolean[][] atlantic = new boolean[rowSize][colSize];

    for (int i = 0; i < rowSize; i++) {
      dfs(i, 0, pacific, heights);
      dfs(i, colSize - 1, atlantic, heights);
    }

    for (int i = 0; i < colSize; i++) {
      dfs(0, i, pacific, heights);
      dfs(rowSize - 1, i, atlantic, heights);
    }

    List<List<Integer>> result = new ArrayList<>();
    for (int i = 0; i < rowSize; i++) {
      for (int j = 0; j < colSize; j++) {
        if (pacific[i][j] && atlantic[i][j]) {
          result.add(List.of(i, j));
        }
      }
    }
    return result;
  }

  private void dfs(int row, int col, boolean[][] visited, int[][] heights) {
    visited[row][col] = true;

    for (int[] direction : directions) {
      int newRow = row + direction[0];
      int newCol = col + direction[1];

      if (newRow < 0 || newRow >= heights.length || newCol < 0 || newCol >= heights[0].length) {
        continue;
      }

      if (visited[newRow][newCol]) {
        continue;
      }

      if (heights[newRow][newCol] < heights[row][col]) {
        continue;
      }

      dfs(newRow, newCol, visited, heights);
    }
  }
}
