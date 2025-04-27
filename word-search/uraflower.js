/**
 * 주어진 2차 배열에 word가 있는지 여부를 반환하는 함수
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
const exist = function (board, word) {
    const row = board.length;
    const col = board[0].length;
    const visited = Array.from({ length: row }, () => Array(col).fill(false));
    const dr = [0, 0, 1, -1];
    const dc = [1, -1, 0, 0];

    function dfs(r, c, charIdx) {

        if (charIdx + 1 === word.length) return true;

        for (let i = 0; i < 4; i++) {
            const nr = r + dr[i];
            const nc = c + dc[i];

            if (0 <= nr && nr < row && 0 <= nc && nc < col && !visited[nr][nc] && word[charIdx + 1] === board[nr][nc]) {
                visited[nr][nc] = true;
                if (dfs(nr, nc, charIdx + 1)) return true;
                visited[nr][nc] = false;
            }
        }

        return false;
    }

    for (let r = 0; r < row; r++) {
        for (let c = 0; c < col; c++) {
            if (word[0] === board[r][c]) {
                visited[r][c] = true;
                if (dfs(r, c, 0)) return true;
                visited[r][c] = false;
            }
        }
    }

    return false;
};

// 시간복잡도: O(m * n * 4^L) (L = word.length. 네 방향으로 최대 L만큼 수행할 수 있음.)
// 공간복잡도: O(m * n)
