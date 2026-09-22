class Solution {

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int n, m;

    public boolean exist(char[][] board, String word) {
        m = board[0].length;
        n = board.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] != word.charAt(0)) continue;

                char cur = board[i][j];
                board[i][j] = '#';
                boolean flag = dfs(board, word, 1, i, j);
                board[i][j] = cur;

                if (flag) return true;
            }
        }

        return false;
    }

    private static boolean dfs(
        char[][] board,
        String word,
        int idx,
        int x,
        int y
    ) {
        if (idx == word.length()) return true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (board[nx][ny] != word.charAt(idx)) continue;

            char cur = board[nx][ny];
            board[nx][ny] = '#';

            boolean flag = dfs(board, word, idx + 1, nx, ny);

            board[nx][ny] = cur;

            if (flag) return true;
        }

        return false;
    }
}
