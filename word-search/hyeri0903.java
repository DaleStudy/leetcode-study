class Solution {
    public boolean exist(char[][] board, String word) {
        /**
        - backtracking (DFS)
        - board[i][j] == word[0] 부터 start
        - 상하좌우 탐색, 같은 칸 중복 탐색 x
        - 틀리면 backtracking

         */

        for(int i = 0; i< board.length; i++) {
            for(int j = 0; j< board[i].length; j++) {
                if(dfs(i, j, 0, board, word)) {
                    return true;
                }
            }
        }
        return false;
    }

    boolean dfs(int i, int j, int index, char[][] board, String word) {
        //모두 다 찾은 경우
        if(index == word.length()) return true;

        //out of bound check
        if(i < 0 || j < 0 || i >= board.length || j>= board[i].length || board[i][j] != word.charAt(index)) return false;

        //방문처리
        char cur = board[i][j];
        board[i][j] = '#';

        //4방향 탐색
        boolean found = dfs(i+1, j, index+1, board, word) || dfs(i-1, j, index+1, board, word) || dfs(i, j+1, index+1, board, word) || dfs(i, j-1, index+1, board, word);

        //backtracking
        board[i][j] = cur;

        return found;
    }
}
