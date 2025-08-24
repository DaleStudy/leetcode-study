class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(board, i, j, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    boolean dfs(char[][] board, int i, int j, String word, int index) {
        if (index == word.length()) return true;
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length) return false; // 범위를 벗어난 경우
        if (board[i][j] != word.charAt(index)) return false; // 일치 조건을 불만족하는 경우

        char temp = board[i][j];
        board[i][j] = '#';
        boolean found = dfs(board, i + 1, j, word, index + 1)
                || dfs(board, i - 1, j, word, index + 1)
                || dfs(board, i, j + 1, word, index + 1)
                || dfs(board, i, j - 1, word, index + 1);

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

    // 백트래킹 인자 국룰 (인자로 받는다는 건 다음에 필요함 + 다음 재귀때 업데이트된 값이 필요해서)
    // 재귀여야 하기 때문에 2차원 input과 방향을 위한 i, j를 받도록 한다.
    // 매번 조건 일치를 확인하기 위한 target 값이 인자로 포함된다 (문제마다 다름)

    // private boolean backtrack (원본 2차원 배열, 타겟, 2차원 방문 배열, i 방향 인덱스, j방향 인덱스, 조건부 target) {
    //    break1. 조건을 만족하면 값을 반환
    //    break2. i와 j의 범위가 0보다 작거나 원본 배열의 길이보다 크거나 같으면 탈락
    //    break3. 방문배열[i][j]가 true거나 (이미 방문했음) 또는 문제의 만족 조건이 아닐 경우 탈락
    // 보통 break2, break3을 한번의 if문으로 작성하지만 난 그마저도 어려워서 한번 더 분리했다.
    //
    //    action1. 방문배열[i][j] 를 true로 설정한다.
    //    action2. i와 j를 위한 2차원 방향배열 템플릿을 선언한다.
    //    action3. 방향은 무조건 동서남북 4방향 고정이다. 4만큼 반복되는 for문을 실행한다.
    //    action3-1. dir[0], dir[1]을 i와 j에게 더해서 nextI, nextJ로 만들어 backtrack()에 전달한다. (이때 조건이 맞으면 return으로 break)
    //    action4. return을 못한 경우 방문배열[i][j]를 false로 재설정한다.
    //    action5. false 등을 리턴한다.
    // }


    private boolean backtrack(char[][] board, String word, boolean[][] visited, int i, int j, int index) {
        if (index == word.length()) {
            return true;
        }

        // dfs를 풀 때는 배열 범위를 벗어나는 경우는 모든 문제 공통이니 그냥 i,j기준으로 0와 length 생각하며 암기
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length) {
            return false;
        }

        if (visited[i][j] || board[i][j] != word.charAt(index)) {
            return false;
        }

        visited[i][j] = true;

        // if문에서 작성하는 것이 눈에 안 익어서
        // direction 템플릿을 만들어서 for문으로 해결하는 암기법으로 변환
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}; // 그냥 암기

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
