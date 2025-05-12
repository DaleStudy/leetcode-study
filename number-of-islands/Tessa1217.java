import java.util.LinkedList;
import java.util.Queue;

/**
 * m x n 2D 행렬 grid가 주어질 때 섬의 수를 찾아서 반환하세요.
 * 섬(island)는 물(0)로 둘러싸여 있고 가로 또는 세로로 인접한 섬들과 연결되어 형성되어 있다.
 */
class Solution {

    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, 1, -1};

    public int numIslands(char[][] grid) {
        int cnt = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                //  land라면
                if (grid[i][j] == '1') {

                    // bfs로 섬 탐색
                    bfs(i, j, grid);

                    // dfs로 섬 탐색
                    dfs(i, j, grid);

                    cnt++;
                }
            }
        }
        return cnt;
    }

    private void dfs(int x, int y, char[][] grid) {
        if (grid[x][y] == '1') {
            grid[x][y] = '0';
        }
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < grid.length && ny >= 0 && ny < grid[0].length && grid[nx][ny] == '1') {
                dfs(nx, ny, grid);
            }
        }
    }

    private void bfs(int startX, int startY, char[][] grid) {

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{startX, startY});
        grid[startX][startY] = '0';

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            for (int i = 0; i < 4; i++) {
                int newX = current[0] + dx[i];
                int newY = current[1] + dy[i];
                if (newX >= 0 && newX < grid.length && newY >= 0 && newY < grid[0].length) {
                    if (grid[newX][newY] == '1') {
                        queue.offer(new int[]{newX, newY});
                        grid[newX][newY] = '0';
                    }
                }
            }
        }
    }
}

