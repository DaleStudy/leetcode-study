class Solution {
    int n;
    int m;
    int[] dx = new int[]{1, 0, -1, 0};
    int[] dy = new int[]{0, 1, 0, -1};

    public int numIslands(char[][] grid) {
        n = grid.length;
        m = grid[0].length;
        boolean[][] visit = new boolean[n][m];
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++){
                if (!visit[i][j] && grid[i][j] == '1') {
                    cnt ++;
                    bfs(i, j, grid, visit);
                }
            }
        }
        return cnt;
    }

    public void bfs(int cx, int cy, char[][] grid, boolean[][] visit) {
        Deque<Point> deque = new ArrayDeque<>();
        visit[cx][cy] = true;
        deque.add(new Point(cx, cy));

        while (!deque.isEmpty()) {
            Point cur = deque.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (outOfRange(nx, ny) || visit[nx][ny] || grid[nx][ny] == '0') continue;
                deque.add(new Point(nx,ny));
                visit[nx][ny] = true;
            }
        }
    }

    public boolean outOfRange(int x, int y) {
        return ((x < 0 || x >= n) || (y < 0 || y >= m));
    }

    static class Point{
        int x;
        int y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}


