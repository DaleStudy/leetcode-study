public class Solution {
    /*
    time complexity: O(M × N × 3^L)
    space complexity: O(M × N + L)
    */
    private int rows, cols;
    private boolean[][] visited;
    private final int[] dx = {0, 1, 0, -1};
    private final int[] dy = {1, 0, -1, 0};

    public boolean exist(char[][] board, String word) {
        rows = board.length;
        cols = board[0].length;
        visited = new boolean[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int x, int y, int idx) {
        if (idx == word.length()) return true;

        if (x < 0 || y < 0 || x >= rows || y >= cols) return false;
        if (visited[x][y] || board[x][y] != word.charAt(idx)) return false;

        visited[x][y] = true;

        for (int d = 0; d < 4; d++) {
            if (dfs(board, word, x + dx[d], y + dy[d], idx + 1)) {
                return true;
            }
        }

        visited[x][y] = false; // 백트래킹
        return false;
    }
}
