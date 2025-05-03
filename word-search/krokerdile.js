/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const rows = board.length;
    const cols = board[0].length;

    // DFS 함수 정의
    const dfs = (r, c, idx) => {
        // 단어 끝까지 찾은 경우
        if (idx === word.length) return true;

        // 범위 밖이거나, 문자 불일치거나, 이미 방문한 경우
        if (
            r < 0 || c < 0 || r >= rows || c >= cols ||
            board[r][c] !== word[idx]
        ) {
            return false;
        }

        const temp = board[r][c]; // 현재 문자 저장
        board[r][c] = "#"; // 방문 표시

        // 상하좌우로 탐색
        const found = dfs(r + 1, c, idx + 1) ||
                      dfs(r - 1, c, idx + 1) ||
                      dfs(r, c + 1, idx + 1) ||
                      dfs(r, c - 1, idx + 1);

        board[r][c] = temp; // 백트래킹: 원상복구

        return found;
    };

    // 보드의 모든 칸에서 시작해보기
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (dfs(r, c, 0)) return true;
        }
    }

    return false;
};

// 시간복잡도: O(m * n * 4^L), m*n번 DFS 시작 가능하고, 각 DFS는 최대 4방향 * 단어 길이 만큼 탐색
