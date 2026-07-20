class Solution {

    private final int[] dx = {-1, 1, 0, 0};
    private final int[] dy = {0, 0, -1, 1};

    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0) && dfs(board, word, i, j, 1)) {
                    return true;
                }
            }
        }

        return false;
    }

    private boolean dfs(char[][] board, String word, int x, int y, int index) {
        if (index == word.length()) return true;

        char tmp = board[x][y];
        board[x][y] = '0';

        for (int i = 0; i < 4; i++) {
            int nextX = x + dx[i], nextY = y + dy[i];
            if (0 <= nextX && nextX < board.length && 0 <= nextY && nextY < board[0].length && board[nextX][nextY] == word.charAt(index)) {
                if(dfs(board, word, nextX, nextY, index + 1)) return true;
            }
        }

        board[x][y] = tmp;

        return false;
    }
}
