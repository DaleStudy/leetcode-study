/**
 * character들로 이루어진 m*n 행렬 board와 word 문자열이 주어질 때 해당 문자열이 행렬 내에 존재할 수 있는지
 * 여부를 불린형으로 반환하세요. (상하좌우로 연결, 셀은 한번만 사용 가능)
 */
class Solution {

    int[] dx = {-1, 1, 0, 0};

    int[] dy = {0, 0, -1, 1};

    int rows, cols;

    // 시간 복잡도: O(M * N * 4^L)
    public boolean exist(char[][] board, String word) {
        rows = board.length;
        cols = board[0].length;

        // 셀 사용 여부를 나타내는 방문 배열
        boolean[][] visited = new boolean[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // 글자의 시작점부터 DFS
                if (board[i][j] == word.charAt(0)) {
                    if (dfs(i, j, 0, visited, board, word)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    // x, y가 board 벗어나지 않는지
    private boolean isRange(int x, int y) {
        return x >= 0 && x < rows && y >= 0 && y < cols;
    }

    // DFS
    private boolean dfs(int x, int y, int idx, boolean[][] visited, char[][] board, String word) {

        if (idx == word.length()) {
            return true;
        }

        if (!isRange(x, y) || visited[x][y] || board[x][y] != word.charAt(idx)) {
            return false;
        }

        visited[x][y] = true;

        // 상하좌우
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (dfs(nx, ny, idx + 1, visited, board, word)) {
                return true;
            }
        }

        visited[x][y] = false;

        return false;

    }
}

