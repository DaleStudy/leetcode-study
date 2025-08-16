class Solution {
    public boolean exist(char[][] board, String word) {
        boolean[][] visited = new boolean[board.length][board[0].length];
        boolean status = false;

        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(word.charAt(0) == board[i][j]){
                    visited[i][j] = true;
                    status = checkingWord(board, word, visited, 1, i, j);
                    visited[i][j] = false;
                }
                if(status) return true;
            }
        }

        return false;
    }
    public boolean checkingWord(char[][] board, String word, boolean[][] visited, int same, int x, int y){
        if(same == word.length()) return true;
        int[] mx = {-1,1,0,0};
        int[] my = {0,0,-1,1};

        for(int k = 0; k < 4; k++){
            int nx = mx[k] + x;
            int ny = my[k] + y;

            if(nx < 0 || ny < 0 || nx >= board.length || ny >= board[0].length) continue;
            if(visited[nx][ny]) continue;

            boolean status = false;

            if(word.charAt(same) == board[nx][ny]){
                visited[nx][ny] = true;
                if(checkingWord(board, word, visited, same + 1, nx, ny)) return true;
                visited[nx][ny] = false;
            }
        }
        return false;
    }
}


