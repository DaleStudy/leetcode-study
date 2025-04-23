// NOTE: Queue를 처음에 써서 탐색하며 꼬여버리는 문제가 있었다..
// NOTE: 원본 문자의 index를 사용해서 해결.

import java.util.LinkedList;
import java.util.Queue;

class Solution {

    public boolean[][] visit;
    int w = 0;
    int h = 0;
    int[] dx = {1, 0, -1, 0};
    int[] dy = {0, 1, 0, -1};
    
    public boolean exist(char[][] board, String word) {

        char[] cArr = word.toCharArray();
        w = board.length;
        h = board[0].length;
        visit = new boolean[w][h];
        
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[0].length; j++) {
                if(cArr[0] == board[i][j]) {                   
                    
                    if(dfs(board, word, i, j, 0)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    public boolean dfs(char[][] b, String word, int x, int y, int idx) {
        if(idx == word.length()) return true;
        
        if(x < 0 || x >= w || y < 0 || y >= h || b[x][y] != word.charAt(idx) || visit[x][y]) {
            return false;
        }

        visit[x][y] = true;

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(dfs(b, word, nx, ny, idx + 1)) {
                return true;
            }
        }

        visit[x][y] = false;
        return false;
    }
    
    
    
    class WrongSolution {

        public boolean[][] visit;
        Queue<Character> q = new LinkedList();
        int w = 0;
        int h = 0;
        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};
        
        public boolean exist(char[][] board, String word) {
    
            char[] cArr = word.toCharArray();
            w = board.length;
            h = board[0].length;
            visit = new boolean[w][h];
            
            for(int i = 0; i < board.length; i++) {
                for(int j = 0; j < board[0].length; j++) {
                    if(cArr[0] == board[i][j]) {
                        q = new LinkedList();
                        visit = new boolean[w][h];
                        for(char c : word.toCharArray()) {
                            q.add(c);
                        }
    
    
                        dfs(board, i, j);
                        if(q.isEmpty()) {
                            return true;
                        }
                    }
                }
            }
    
            return false;
        }
    
        public void dfs(char[][] b, int x, int y) {
            if(x < 0 || x >= w || y < 0 || y >= h || visit[x][y]) {
                return;
            }
    
            if(q.isEmpty()) {
                return;
            }
    
            if(b[x][y] != q.peek()) {
                return;
            }
    
            q.poll();
            visit[x][y] = true;
            
            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
    
                dfs(b, nx, ny);
            }
        }
    }}