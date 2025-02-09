// 189ms가 나와서 다시 시도해볼 예정
class Solution {
    private int[] rowMove = {1, -1, 0, 0};
    private int[] colMove = {0, 0, 1, -1};

    public boolean exist(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int row, int col, int index) {
        if (index == word.length()) {
            return true;
        }

        if (row < 0 || col < 0 || row >= board.length || col >= board[0].length || board[row][col] != word.charAt(index)) {
            return false;
        }

        char temp = board[row][col];
        board[row][col] = '#'; 

        for (int i = 0; i < 4; i++) {
            int newRow = row + rowMove[i];
            int newCol = col + colMove[i];
            if (dfs(board, word, newRow, newCol, index + 1)) {
                return true;
            }
        }

        board[row][col] = temp;

        return false;
    }
}
