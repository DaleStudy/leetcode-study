class Solution {
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    public boolean exist(char[][] board, String word) {
        /**
        1. understanding
        - check if word can be constructed from board,
        - start in any block, moving only 4 direction, up, left, below, right
        - can't use same block
        2. strategy
        - backtracking and dfs
            - iterate over each block, if first character matches, find words in depth first search algorithm
            - each dfs, mark current block is visited, and find 4 or less possible directions, when any character matches with next character in word, then call dfs in that block recursively
        3. complexity
        - time: O(M * N * L), where L is the length of word
        - space: O(M * N) which marks if block of the indices is visited or not
        */
        boolean[][] isVisited = new boolean[board.length][board[0].length];
        for (int y = 0; y < board.length; y++) {
            for (int x = 0; x < board[0].length; x++) {
                if (isWordExists(board, isVisited, word, y, x, 0)) return true;
            }
        }
        return false;
    }

    private boolean isWordExists(char[][] board, boolean[][] isVisited, String word, int y, int x, int idx) {
        if (board[y][x] != word.charAt(idx)) return false;
        if (idx == word.length() - 1) return true;
        // boolean isExists = false;
        isVisited[y][x] = true;
        for (int dir = 0; dir < 4; dir++) {
            int ny = y + dy[dir];
            int nx = x + dx[dir];
            if (0 <= ny && ny < board.length 
            && 0 <= nx && nx < board[0].length 
            && !isVisited[ny][nx] 
            && word.charAt(idx + 1) == board[ny][nx]) {
                isVisited[ny][nx] = true;
                if (isWordExists(board, isVisited, word, ny, nx, idx + 1)) return true;
                isVisited[ny][nx] = false;
            }
        }
        isVisited[y][x] = false;
        return false;
    }
}

