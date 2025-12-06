class Solution {
    public boolean exist(char[][] board, String word) {

        int rows = board.length;
        int columns = board[0].length;
        boolean[][] visited = new boolean[rows][columns];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (dfs(board, word, i, j, 0, visited)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int row, int col, int idx, boolean[][] visited) {
        //예외 처리 1
        if (idx == word.length()) return true;

        //예외 처리 2
        if (row < 0 || col < 0 || row >= board.length || col >= board[0].length) return false;

        //예외 처리 3
        if (visited[row][col]) return false;

        //1. 글자 체크
        if (board[row][col] != word.charAt(idx)) return false;

        //방문 처리
        visited[row][col] = true;

        //상, 하, 좌, 우 찾기
        boolean found = dfs(board, word, row + 1, col, idx + 1, visited)
                || dfs(board, word, row - 1, col, idx + 1, visited)
                || dfs(board, word, row, col + 1, idx + 1, visited)
                || dfs(board, word, row, col - 1, idx + 1, visited);

        visited[row][col] = false;
        return found;
    }
}
