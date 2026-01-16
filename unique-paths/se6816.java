class Solution {
    public int[] moveX = {0, 1};
    public int[] moveY = {1, 0};
    int N;
    int M;
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        boolean[][] visited = new boolean[m][n];
        int curX = 0;
        int curY = 0;
        N = n;
        M = m;
        dp[curX][curY] = 1;
        visited[curX][curY] = true;
        Queue<int[]> que = new ArrayDeque<>();
        que.offer(new int[]{0,0});

        while(!que.isEmpty()) {
            int[] data = que.poll();

            for(int i = 0; i < 2; i++) {
                int tempX = data[0] + moveX[i];
                int tempY = data[1] + moveY[i];

                if(isOutOfIndex(tempX, tempY)) {
                    continue;
                }

                dp[tempX][tempY] += dp[data[0]][data[1]];


                if(visited[tempX][tempY]) {
                    continue;
                }
                visited[tempX][tempY] = true;
                que.add(new int[]{tempX, tempY});

            }
        }

        return dp[M-1][N-1];

    }

    public boolean isOutOfIndex(int x, int y) {
        return x < 0 || x >= M || y < 0 || y >=N;
    }
}
