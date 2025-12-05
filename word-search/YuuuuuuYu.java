/**
 * Runtime: 130ms
 * Time Complexity: O(m x n x 4^l)
 * - m: board의 행 길이
 * - n: board의 열 길이
 * - l: word의 길이
 *
 * Memory: 42.32MB
 * Space Complexity: O(l)
 *
 * Approach: DFS + 백트래킹
 * 1) board를 순회하며 word의 첫 글자와 일치하는 글자를 찾음
 * 2) 일치하는 글자를 찾으면 DFS를 통해 상하좌우로 다음 글자를 찾음
 * 3) 성능 최적화
 * - 백트래킹을 위해 방문한 글자는 임시로 다른 문자('#')로 변경 (비트마스크)
 * - charAt 캐싱
 */
class Solution {
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};

    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        char startChar = word.charAt(0);

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (board[i][j] == startChar) {
                    if (dfs(board, i, j, 0, word)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    private boolean dfs(char[][] board, int x, int y, int index, String word) {
        if (index == word.length()-1) {
            return true;
        }

        char temp = board[x][y];
        char nextChar = word.charAt(index+1);
        board[x][y] = '#';

        for (int i=0; i<4; i++) {
            int nx = x+dx[i];
            int ny = y+dy[i];

            if (nx >= 0 && nx < board.length &&
                    ny >= 0 && ny < board[0].length &&
                    board[nx][ny] == nextChar) {

                if (dfs(board, nx, ny, index+1, word)) {
                    board[x][y] = temp;
                    return true;
                }
            }
        }

        board[x][y] = temp;
        return false;
    }
}
