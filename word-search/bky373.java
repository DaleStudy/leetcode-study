/*
 * time: O(N * 4^L)
 *  - N: the number of cells in the board
 *  - L: the length of the word
 *  - 4: the length of directions
 * space: O(L)
 *  - L: the recursive backtracking function call stacks.
 */
class Solution {

    private char[][] board;
    private int rLen;
    private int cLen;

    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.rLen = board.length;
        this.cLen = board[0].length;

        for (int row = 0; row < this.rLen; ++row) {
            for (int col = 0; col < this.cLen; ++col) {
                if (this.backtrack(row, col, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean backtrack(int row, int col, String word, int matchIndex) {
        if (matchIndex >= word.length()) {
            return true;
        }

        if (row < 0 || row == this.rLen || col < 0 || col == this.cLen || this.board[row][col] != word.charAt(matchIndex)) {
            return false;
        }

        this.board[row][col] = ' ';

        int[] rowDirs = {0, 1, 0, -1};
        int[] colDirs = {1, 0, -1, 0};
        for (int dir = 0; dir < 4; ++dir) {
            if (backtrack(row + rowDirs[dir], col + colDirs[dir], word, matchIndex + 1)) {
                return true;
            }
        }

        this.board[row][col] = word.charAt(matchIndex);
        return false;
    }
}
