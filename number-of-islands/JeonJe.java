import java.util.*;

// TC: O(m * n)
// SC: O(m * n)
class Solution {

    private static int[] dx = {0, -1, 0, 1};
    private static int[] dy = {1, 0, -1, 0};

    private int n = 0;
    private int m = 0;

    public int numIslands(char[][] grid) {
        n = grid[0].length;
        m = grid.length;

        boolean[][] visited = new boolean[m][n];

        int answer = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && grid[i][j] == '1') {
                    answer++;
                    dfs(i, j, grid, visited);
                }
            }
        }
        return answer;
    }

    private void dfs(int x, int y, char[][] grid, boolean[][] visited) {
        visited[x][y] = true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < m && 0 <= ny && ny < n && grid[nx][ny] == '1' && !visited[nx][ny]) {
                dfs(nx, ny, grid, visited);
            }
        }
    }
}
