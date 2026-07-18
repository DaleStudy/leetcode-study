import java.util.*;

// TC: O(m * n * 4^L)
// SC: O(m * n)
class Solution {

    private char[][] board;
    private int m, n;
    private boolean[][] visited;
    private char[] word;
    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};


    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.word = word.toCharArray();
        this.n = board.length;
        this.m = board[0].length;
        this.visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (dfs(i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(int x, int y, int wordIndex) {
        if (board[x][y] != word[wordIndex] || visited[x][y]) {
            return false;
        }
        if (wordIndex == word.length - 1) {
            return true;
        }

        visited[x][y] = true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }

            if (board[nx][ny] == word[wordIndex + 1] && !visited[nx][ny]) {
                if (dfs(nx, ny, wordIndex + 1)) {
                    return true;
                }
            }
        }
        visited[x][y] = false;
        return false;
    }
}
