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

    // 2차원 방문 배열을 만들고 direction 방향 템플릿으로 풀이
    public boolean exist2(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        boolean[][] visited = new boolean[m][n];
        boolean result = false;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word.charAt(0)) {
                    result = backtrack(board, word, visited, i, j, 0);
                    if (result)
                        return true;
                }
            }
        }

        return false;
    }

    private boolean backtrack(char[][] board, String word, boolean[][] visited, int i, int j, int index) {
        if (index == word.length()) {
            return true;
        }

        // dfs를 풀 때는 배열 범위를 벗어나는 경우 break를 꼭 기억하기
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || visited[i][j]
                || board[i][j] != word.charAt(index)) {
            return false;
        }

        visited[i][j] = true;

        // if문에서 작성하는 것이 눈에 안 익어서
        // direction 템플릿을 만들어서 for문으로 해결하는 암기법으로 변환
        int[][] directions = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } }; // 그냥 암기

        for (int[] dir : directions) {
            // i가 y, j가 x인데 사실 1, -1, 0만 잘 설정하면 상관없음. 목적은 1, -1 1번씩 그리고 나머지는 0으로 채우는 것
            int nextI = i + dir[0];
            int nextJ = j + dir[1];

            if (backtrack(board, word, visited, nextI, nextJ, index + 1)) {
                return true;
            }
        }

        visited[i][j] = false;
        return false;
    }

}
