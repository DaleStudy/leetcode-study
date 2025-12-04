
/**
    DFS를 통해 이중 배열에서 문자를 찾는 방식
    board의 길이 -> M
    board[i]의 길이 -> N
    시간 복잡도 : O(M*N)
    공간 복잡도 : O(M*N)
 */
class Solution {
    public static int[] moveX = {0, -1, 1, 0};
    public static int[] moveY = {-1, 0, 0, 1};
    public int N;
    public int M;
    public boolean exist(char[][] board, String word) {
        M = board.length;
        N = board[0].length;
        boolean result = false;
        char startCh = word.charAt(0);
        for(int i = 0; i < M; i++) {
            for(int j = 0; j < N; j++) {
                if(board[i][j] != startCh) {
                    continue;
                }
                boolean[][] visited = new boolean[M][N];
                visited[i][j] = true;
                result = result || search(board, visited, i, j, 1, word);
            }
        }
        return result;
    }

    public boolean search(char[][] board, boolean[][] visited, int x, int y, int len, String target) {
        if(len >= target.length()) {
            return true;
        }

        boolean result = false;

        for(int i = 0; i < 4; i++) {
            int tempX = x + moveX[i];
            int tempY = y + moveY[i];

            if(outOfIndex(tempX, tempY)) {
                continue;
            }

            if(visited[tempX][tempY]) {
                continue;
            }

            if(board[tempX][tempY] != target.charAt(len)) {
                continue;
            }

            visited[tempX][tempY] = true;
            result = search(board, visited, tempX, tempY, len + 1, target) || result;
            if(result) {
                break;
            }
            visited[tempX][tempY] = false;
        }

        return result;
    }

    public boolean outOfIndex(int x, int y){
        if(x < 0 || x >= M || y < 0 || y >= N) {
            return true;
        }

        return false;
    }
}
