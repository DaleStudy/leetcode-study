class Solution {
    int m, n;
    int[] dx = new int[]{0, 1, 0, -1};
    int[] dy = new int[]{1, 0, -1, 0};
    boolean answer = false;
    boolean[][] visit;

    public boolean exist(char[][] board, String word) {
        m = board.length;
        n = board[0].length;
        visit = new boolean[m][n];

        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (board[i][j] == word.charAt(0)){
                    visit[i][j] = true;
                    dfs(i, j, board, word, 0);
                    visit[i][j] = false;
                }
            }
        }
        return answer;
    }

    public void dfs(int cx, int cy, char[][] board, String word, int depth){
        if (depth == word.length()-1){
            answer = true;
            return;
        }

        for (int i = 0; i < 4; i++){
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            int nextDepth = depth + 1;

            if (outOfRange(nx, ny)||visit[nx][ny]) continue;
            if (board[nx][ny] == word.charAt(nextDepth)){
                visit[nx][ny] = true;
                dfs(nx, ny, board, word, nextDepth);
                visit[nx][ny] = false;
            }
        }
    }

    public boolean outOfRange(int x, int y){
        return (x < 0 || x >= m) || (y < 0 || y >= n);
    }
}


