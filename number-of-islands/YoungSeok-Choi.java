import java.util.LinkedList;
import java.util.Queue;

class Solution {

    public int[] dx = { 1, 0, -1, 0 };
    public int[] dy = { 0, 1, 0, -1 };
    public int cnt = 0;
    public int w = 0;
    public int h = 0;
    public boolean[][] visit;
    public Queue<Node> q = new LinkedList<>();

    public int numIslands(char[][] grid) {
        w = grid.length;
        h = grid[0].length;
        visit = new boolean[w][h];

        for (int i = 0; i < w; i++) {
            for (int j = 0; j < h; j++) {
                if (grid[i][j] == '1') {
                    cnt++;
                    // dfs(grid, i, j);
                    bfs(grid, i, j);
                }
            }
        }

        return cnt;
    }

    public void dfs(char[][] grid, int x, int y) {
        if (x < 0 || x >= w || y < 0 || y >= h || grid[x][y] == '0' || visit[x][y]) {
            return;
        }

        visit[x][y] = true;
        grid[x][y] = '0';

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            dfs(grid, nx, ny);
        }
    }

    public void bfs(char[][] grid, int x, int y) {

        q.add(new Node(x, y));

        while (!q.isEmpty()) {
            Node p = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];

                if (x < 0 || x >= w || y < 0 || y >= h || grid[x][y] == '0' || visit[x][y]) {
                    continue;
                }

                grid[nx][ny] = '0';
                q.add(new Node(nx, ny));
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
