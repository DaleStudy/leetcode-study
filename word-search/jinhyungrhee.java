class Solution {
    public boolean exist(char[][] board, String word) {

        boolean[][] visited = new boolean[board.length][board[0].length];

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if(dfs(board, word, visited, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean dfs(char[][] board, String word, boolean[][] visited, int x, int y, int index) {

        // [성공] : 모든 글자 매칭 성공
        if (index == word.length()) return true;

        // [실패] : 범위 초과, 방문함, 글자 불일치
        if (x < 0 || x >= board.length || y < 0 || y >= board[0].length ||
                visited[x][y] || board[x][y] != word.charAt(index)) {
            return false;
        }

        visited[x][y] = true;
        int[][] dir = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
        for (int i = 0; i < 4; i++) {
            int newX = x + dir[i][0], newY = y + dir[i][1];
            if (dfs(board, word, visited, newX, newY, index + 1)) {
                return true; // 찾았으면 바로 리턴
            }
        }
        visited[x][y] = false; // backtrack

        return false; // 4방향 다 실패하면 false

    }
}
