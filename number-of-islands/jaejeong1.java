class SolutionNumberOfIslands {
  char[][] sharedGrid;
  int[] dx = new int[]{0, 0, -1, 1};
  int[] dy = new int[]{-1, 1, 0, 0};

  public int numIslands(char[][] grid) {
    // 풀이
      // 네 모서리가 물로 둘러쌓여있으면 아일랜드
      // 아일랜드의 개수를 반환해라
      // 땅인 경우 DFS 돌려서 순회하자
      // 상하좌우 확인하면서 땅이면 물로 변경하면서 순회한다
      // DFS 1회 당 answer += 1
    // TC: O(N), N은 배열 원소 개수
    // SC: O(N)
    var answer = 0;

    sharedGrid = grid;
    for (int i=0; i<grid.length; i++) {
      for (int j=0; j<grid[0].length; j++) {
        if (sharedGrid[i][j] == '1') {
          dfs(i, j);
          answer++;
        }
      }
    }

    return answer;
  }

  private void dfs(int i, int j) {
    sharedGrid[i][j] = '0';

    for (int k=0; k<4; k++) {
      var x = i+dx[k];
      var y = j+dy[k];
      if (x >= 0 && y >= 0 && x < sharedGrid.length && y < sharedGrid[0].length && sharedGrid[x][y] == '1') {
        dfs(x, y);
      }
    }
  }
}
