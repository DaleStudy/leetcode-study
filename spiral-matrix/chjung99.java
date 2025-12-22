class Solution {
    // right, down, left, up
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    boolean[][] visit;

    int m;
    int n;
    public List<Integer> spiralOrder(int[][] matrix) {
        m = matrix.length;
        n = matrix[0].length;
        visit = new boolean[m][n];
        return bfs(matrix);
    }

    public boolean outOfRange(int x, int y){
        return ((x < 0 || x >= m) || (y < 0 || y >= n));
    }

    public List<Integer> bfs(int[][] matrix) {
        List<Integer> spiral = new ArrayList<>();

        Queue<Point> q = new ArrayDeque<>();

        int startX = 0;
        int startY = 0;
        int startDir = 0;

        q.add(new Point(startX, startY, startDir));
        visit[startX][startY] = true;

        while (!q.isEmpty()){
            Point cur = q.poll();
            spiral.add(matrix[cur.x][cur.y]);

            int nextX = cur.x + dx[cur.dir];
            int nextY = cur.y + dy[cur.dir];
            int nextDir = cur.dir;

            if (outOfRange(nextX, nextY) || visit[nextX][nextY]) {
                nextDir = (nextDir + 1) % 4;
            }

            nextX = cur.x + dx[nextDir];
            nextY = cur.y + dy[nextDir];

            if (!outOfRange(nextX, nextY) && !visit[nextX][nextY]){
                q.add(new Point(nextX, nextY, nextDir));
                visit[nextX][nextY] = true;
            }
        }
        return spiral;
    }

    class Point{
        int x;
        int y;
        int dir;
        public Point(int x, int y, int dir){
            this.x = x;
            this.y = y;
            this.dir = dir;
        }
    }

}


