/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 *
 * 문제: https://leetcode.com/problems/word-search/
 * 요구사항: 그리드 구조에서 word의 문자열 존재 여부에 따라 true/false를 리턴한다.
 * 백트래킹, dfs
 */
const exist = (board, word) => {
    let rows = board.length;
    let cols = board[0].length;

    const dfs = (r, c, index) => {
        if (index === word.length) return true;

        if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] !== word[index]) {
            return false;
        }

        let temp = board[r][c];
        board[r][c] = '#';

        let found = dfs(r + 1, c, index + 1) ||
            dfs(r - 1, c, index + 1) ||
            dfs(r, c + 1, index + 1) ||
            dfs(r, c - 1, index + 1);

        board[r][c] = temp;

        return found;
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (board[i][j] === word[0] && dfs(i, j, 0)) return true;
        }
    }

    return false;
};
