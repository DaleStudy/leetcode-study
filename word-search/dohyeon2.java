class Solution {
    // TC : O(n*4^L); n = the number of the characters, L = the length of the word
    // SC : O(m*n + L) m = a row of the board, n = a cell of the board, L = the length of the word
    public boolean exist(char[][] board, String word) {
        for (int y = 0; y < board.length; y++) {
            for (int x = 0; x < board[0].length; x++) {
                if(board[y][x] != word.charAt(0)){
                    continue;
                }
                boolean[][] visited = new boolean[board.length][board[0].length];
                if (backtrack(x, y, 0, board, visited, word)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean backtrack(int x, int y, int index, char[][] board, boolean[][] visited, String word) {
        if (index == word.length())
            return true;

        if (y < 0 || y >= board.length || x < 0 || x >= board[0].length)
            return false;

        if (visited[y][x] || board[y][x] != word.charAt(index))
            return false;

        visited[y][x] = true;

        boolean found = backtrack(x + 1, y, index + 1, board, visited, word) ||
                backtrack(x - 1, y, index + 1, board, visited, word) ||
                backtrack(x, y + 1, index + 1, board, visited, word) ||
                backtrack(x, y - 1, index + 1, board, visited, word);

        visited[y][x] = false; // It failed on the first attempt because this line was missing.

        return found;
    }

}
