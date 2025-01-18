class Solution {

  public int uniquePaths(int m, int n) {
    int[][] paths = new int[m][n];

    for (int i = 0; i < m; i++) {
      paths[i][0] = 1; //가장 왼쪽 줄은 항상 경로가 1개
    }

    for (int i = 0; i < n; i++) {
      paths[0][i] = 1; // 가장 윗줄은 항상 경로가 1개
    }
    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {

        paths[i][j] = paths[i - 1][j] + paths[i][j - 1];
      }
    }

    return paths[m - 1][n - 1];
  }
}
