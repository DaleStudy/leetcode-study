/*
Time Complexity: O(m * n * 4^(word.length))
Space Complexity: O(m * n)
*/

class Solution {
    boolean[][] visited;
    int m, n;
    int len;
    int[] dr = {-1, 0, 1, 0}; // clockwise traversal
    int[] dc = {0, 1, 0, -1};
    char board2[][];
    String word2;

    public boolean exist(char[][] board, String word) {
        int[] cnt = new int[52];
        board2 = board;
        word2 = word;
        m = board.length;
        n = board[0].length;
        visited = new boolean[m][n];
        len = word.length();

        // 1. for pruning, count characters in board and word respectively
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cnt[charToInt(board[i][j])]++;
            }
        }
        for (int i = 0; i < len; i++) {
            int idx = charToInt(word.charAt(i));
            if (--cnt[idx] < 0) {
                return false;
            }
        }

        // 2. DFS
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board2[i][j] != word.charAt(0)) {
                    continue;
                }
                if (dfs(i, j, 1)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(int row, int col, int idx) {
        if (idx == len) { // end of word
            return true;
        }
        visited[row][col] = true;

        for (int i = 0; i < 4; i++) {
            int nr = row + dr[i];
            int nc = col + dc[i];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) { // check boundary of the board
                continue;
            }
            if (visited[nr][nc]) { // check visited
                continue;
            }
            if (board2[nr][nc] == word2.charAt(idx)) {
                if (dfs(nr, nc, idx + 1)) {
                    return true;
                }
            }
        }

        visited[row][col] = false;
        return false;
    }

    private int charToInt(char ch) {
        if (ch <= 'Z') {
            return ch - 'A';
        } else {
            return ch - 'a' + 26;
        }
    }
}
