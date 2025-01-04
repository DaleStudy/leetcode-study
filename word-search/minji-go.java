/*
    Problem: https://leetcode.com/problems/word-search/
    Description: return true if word exists in the grid
    Concept: Array, String, Backtracking, Matrix
    Time Complexity: O(MN4ᵀ), Runtime 147ms
    Space Complexity: O(MN), Memory 42.11MB
*/
class Solution {
    public char[][] board;
    public String word;
    public boolean[][] visited;
    public int n, m;

    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.word = word;
        this.m = board.length;
        this.n = board[0].length;
        this.visited = new boolean[m][n];

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(word.charAt(0) != board[i][j]) continue;
                if(wordExists(i, j, 1)) return true;
            }
        }
        return false;
    }

    public int[] dr = new int[]{-1,1,0,0};
    public int[] dc = new int[]{0,0,-1,1};
    public boolean wordExists(int cr, int cc, int i){
        if(i==word.length()) return true;

        visited[cr][cc] = true;
        for(int k=0; k<4; k++){
            int nr = cr+dr[k];
            int nc = cc+dc[k];
            if(nr<0||nc<0||nr>m-1||nc>n-1||visited[nr][nc]) continue;
            if(board[nr][nc]!=word.charAt(i)) continue;
            if(wordExists(nr, nc, i+1)) return true;
        }
        visited[cr][cc] = false;

        return false;
    }
}
