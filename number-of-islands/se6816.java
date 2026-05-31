/**
    방문하지 않는 지점을 찾고, BFS로 인근 지점을 방문처리하며, 방문하지 않는 지점 개수를 카운틷하는 방식
 */
class Solution {
    int M;
    int N;
    boolean[][] visited;
    int[] moveX = {-1, 0, 0, 1};
    int[] moveY = {0, -1, 1, 0};
    public int numIslands(char[][] grid) {
        int result = 0;
        M = grid.length;
        N = grid[0].length;
        visited= new boolean[M][N];
        for(int i = 0; i < M; i++) {
            for(int j = 0; j < N; j++) {
                if(!visited[i][j] && grid[i][j] == '1') {
                    visited[i][j] = true;
                    result++;
                    paint(i, j, visited, grid);
                }
            }
        }
        return result;
        
    }
    public void paint(int x, int y, boolean[][] visited, char[][] grid) {
        for(int i = 0; i < 4; i++) {
            int tempX = x + moveX[i];
            int tempY = y + moveY[i];

            if(isOutOfIndex(tempX, tempY)) {
                continue;
            }

            if(visited[tempX][tempY]) {
                continue;
            }

            if(grid[tempX][tempY] == '0') {
                continue;
            }

            visited[tempX][tempY] = true;

            paint(tempX,tempY, visited, grid);
        }
    }
    public boolean isOutOfIndex(int x, int y) {
        return x < 0 || x >= M || y < 0 || y >=N;
    }
}
