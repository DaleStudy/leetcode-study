/**
  * [풀이 개요]
  * - 시간복잡도 : O(N * M * 3^L) 
  *   (N, M은 격자 크기, L은 단어의 길이. 각 칸에서 사방 탐색 시 이전 칸을 제외한 3방향으로 최대 L번 재귀 호출)
  * - 공간복잡도 : O(N * M) 
  *   (N * M 크기의 visited 배열 및 최대 L 깊이의 재귀 호출 스택 사용)
  */
class Solution {
    // 세로(row), 가로(col) 이동을 위한 오프셋
    // dy -> dRow (상하 이동), dx -> dCol (좌우 이동)
    int[] dRow = { 0, 1, 0, -1 };
    int[] dCol = { 1, 0, -1, 0 };

    public boolean exist(char[][] board, String word) {
        int maxRow = board.length;       // 세로 길이 (limitY)
        int maxCol = board[0].length;    // 가로 길이 (limitX)

        // visited 배열도 board와 동일하게 [row][col] 크기로 선언
        boolean[][] visited = new boolean[maxRow][maxCol];
        char startChar = word.charAt(0);

        for (int r = 0; r < maxRow; r++) {
            for (int c = 0; c < maxCol; c++) {
                if (startChar == board[r][c]) {
                    // 첫 글자가 일치하면 백트래킹 시작
                    if (find(1, word.length(), r, c, maxRow, maxCol, board, word, visited)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    public boolean find(
        int cursor, 
        int len,
        int curRow, 
        int curCol, 
        int maxRow,
        int maxCol, 
        char[][] board,
        String word, 
        boolean[][] visited
    ) {
        // 기저 조건: 단어를 모두 완성한 경우
        if (cursor >= len) {
            return true; 
        }

        // 현재 좌표 방문 처리
        visited[curRow][curCol] = true;

        for (int i = 0; i < 4; i++) {
            int nextRow = curRow + dRow[i];
            int nextCol = curCol + dCol[i];

            // 1. 격자 경계선 체크
            if (nextRow < 0 || nextRow >= maxRow || nextCol < 0 || nextCol >= maxCol) {
                continue;
            }

            // 2. 방문하지 않았고, 다음 목표 문자와 일치하는지 체크
            if (!visited[nextRow][nextCol]) {    
                char nextChar = board[nextRow][nextCol];
                
                if (word.charAt(cursor) == nextChar) {    
                    if (find(cursor + 1, len, nextRow, nextCol, maxRow, maxCol, board, word, visited)) {
                        return true;
                    }
                }
            }
        }

        // 탐색이 실패로 끝나면 현재 좌표 방문 해제 (Backtrack)
        visited[curRow][curCol] = false;
        
        return false;
    }
}
