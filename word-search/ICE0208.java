class Solution {
    private static final int[][] DIRECTIONS = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}
    };

    private char[][] board;
    private String word;
    private boolean[][] visited;
    private int rows;
    private int cols;

    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.word = word;
        this.rows = board.length;
        this.cols = board[0].length;
        this.visited = new boolean[rows][cols];

        // 단어가 전체 칸보다 길면 경로를 만들 수 없다.
        if (word.length() > rows * cols) {
            return false;
        }

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                // 첫 문자가 일치하는 위치에서만 탐색을 시작한다.
                if (board[row][col] == word.charAt(0)
                        && search(row, col, 0)) {
                    return true;
                }
            }
        }

        return false;
    }

    private boolean search(int row, int col, int wordIndex) {
        // 이미 현재 경로에서 사용한 칸이거나 문자가 다르면 탐색을 중단한다.
        if (visited[row][col]
                || board[row][col] != word.charAt(wordIndex)) {
            return false;
        }

        // 마지막 문자까지 일치했다면 단어를 찾은 것이다.
        if (wordIndex == word.length() - 1) {
            return true;
        }

        visited[row][col] = true;

        for (int[] direction : DIRECTIONS) {
            int nextRow = row + direction[0];
            int nextCol = col + direction[1];

            if (!isInBounds(nextRow, nextCol)) {
                continue;
            }

            if (search(nextRow, nextCol, wordIndex + 1)) {
                visited[row][col] = false;
                return true;
            }
        }

        // 다른 경로에서 현재 칸을 다시 사용할 수 있도록 방문 상태를 복구한다.
        visited[row][col] = false;
        return false;
    }

    private boolean isInBounds(int row, int col) {
        return row >= 0 && row < rows
                && col >= 0 && col < cols;
    }
}
