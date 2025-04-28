/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const rows = board.length;
    const cols = board[0].length;

    function backtrack(r, c, index) {
        // 모든 문자를 다 찾았으면 true 반환
        if (index === word.length) return true;

        // 경계 조건 및 현재 문자가 일치하지 않으면 false
        if (
            r < 0 || r >= rows ||
            c < 0 || c >= cols ||
            board[r][c] !== word[index]
        ) {
            return false;
        }

        // 현재 위치 문자 저장 후, 방문 표시로 덮어쓰기
        const temp = board[r][c];
        board[r][c] = '#';

        // 4방향 탐색: 상하좌우
        const directions = [[-1,0], [1,0], [0,-1], [0,1]];
        for (const [dr, dc] of directions) {
            if (backtrack(r + dr, c + dc, index + 1)) {
                return true;
            }
        }

        // 상태 복구
        board[r][c] = temp;
        return false;
    }

    // 모든 위치에서 시작 가능
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (backtrack(i, j, 0)) return true;
        }
    }

    return false;
};
