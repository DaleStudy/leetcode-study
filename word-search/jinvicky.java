class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(dfs(board, i, j, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    boolean dfs(char[][] board,int i,int j,String word,int index){
        if(index == word.length()) return true;
        if(i<0 || j<0 || i>=board.length || j>=board[0].length) return false; // 범위를 벗어난 경우
        if(board[i][j] != word.charAt(index)) return false; // 일치 조건을 불만족하는 경우

        char temp = board[i][j];
        board[i][j] = '#';
        boolean found = dfs(board, i+1, j, word, index+1)
                || dfs(board, i-1, j, word, index+1)
                || dfs(board, i, j+1, word, index+1)
                || dfs(board, i, j-1, word, index+1);

        board[i][j] = temp;
        return found;
    }

}