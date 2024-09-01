// TC: O(n * m * 4^k);
// -> The size of board: n * m
// -> Check 4 directions by the given word's length: 4^k
// SC: O(n * m + k)
// -> boolean 2D array: n * M
// -> recursive max k spaces
class Solution {
    public boolean exist(char[][] board, String word) {
        // Mark visited path to do not go back.
        boolean[][] visit = new boolean[board.length][board[0].length];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (wordSearch(i, j, 0, word, board, visit)) return true;
            }
        }
        return false;
    }

    private boolean wordSearch(int i, int j, int idx, String word, char[][] board, boolean[][] visit) {

        // When idx checking reach to the end of the length of the word then, return true
        if (idx == word.length()) return true;

        // Check if i and j are inside of the range
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length) return false;

        // Check if the coordinate equals to the charactor value
        if (board[i][j] != word.charAt(idx)) return false;
        if (visit[i][j]) return false;

        // Mark the coordinate as visited
        visit[i][j] = true;

        // If visited, the target is gonna be the next charactor
        idx += 1;

        // If any direction returns true then it is true
        if (
            wordSearch(i+1, j, idx, word, board, visit) ||
            wordSearch(i-1, j, idx, word, board, visit) ||
            wordSearch(i, j+1, idx, word, board, visit) ||
            wordSearch(i, j-1, idx, word, board, visit)
        ) return true;

        // If visited wrong direction, turns it as false
        visit[i][j] = false;

        return false;
    }
}
