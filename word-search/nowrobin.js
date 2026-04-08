/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const rows = board.length;
    const cols = board[0].length;

    function dfs(r, c, index) {
        if (r < 0 || c < 0 || r >= rows || c >= cols) return false;
        if (board[r][c] !== word[index]) return false;

        if (index === word.length - 1) return true;

        const temp = board[r][c];
        board[r][c] = "#";

        const found =
            dfs(r + 1, c, index + 1) ||
            dfs(r - 1, c, index + 1) ||
            dfs(r, c + 1, index + 1) ||
            dfs(r, c - 1, index + 1);

        board[r][c] = temp;

        return found;
    }

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (dfs(r, c, 0)) return true;
        }
    }

    return false;
};
