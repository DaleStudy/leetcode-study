class Solution {
    public boolean exist(char[][] board, String word) {
        if (board == null || board.length == 0 || word == null || word.length() == 0) {
            return false;
        }

        int rows = board.length;
        int cols = board[0].length;
        boolean[][] visited = new boolean[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(board, visited, i, j, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private static boolean dfs(char[][] board, boolean[][] visited, int i, int j, String word, int index) {
        if (index == word.length()) {
            return true;
        }

        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || visited[i][j] || board[i][j] != word.charAt(index)) {
            return false;
        }


        visited[i][j] = true;

        boolean found = dfs(board, visited, i + 1, j, word, index + 1) ||
                dfs(board, visited, i - 1, j, word, index + 1) ||
                dfs(board, visited, i, j + 1, word, index + 1) ||
                dfs(board, visited, i, j - 1, word, index + 1);

        visited[i][j] = false;

        return found;
    }
}
