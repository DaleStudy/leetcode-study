import java.util.ArrayList;
import java.util.List;

class Solution {

  public List<Node> point = new ArrayList<>();

  public void setZeroes(int[][] matrix) {

    for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix[0].length; j++) {
        if (matrix[i][j] == 0) {
          point.add(new Node(i, j));
        }
      }
    }

    for (Node n : point) {
      int x = n.x;
      int y = n.y;

      int nx = n.x;
      while (nx > 0) {
        matrix[--nx][y] = 0;
      }

      int ny = n.y;
      while (ny > 0) {
        matrix[x][--ny] = 0;
      }

      int nnx = n.x;
      while (nnx < matrix.length - 1) {
        matrix[++nnx][y] = 0;
      }

      int nny = n.y;
      while (nny < matrix[0].length - 1) {
        matrix[x][++nny] = 0;
      }
    }
  }

}

class Node {
  int x;
  int y;

  public Node(int x, int y) {
    this.x = x;
    this.y = y;
  }
}
