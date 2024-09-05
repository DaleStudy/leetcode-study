/**
 * https://leetcode.com/problems/word-search
 * time complexity : O(m * n * 4^L)
 * space complexity : O(L)
 */
const dfs = (r: number, c: number, index: number, board: string[][], word: string, rows: number, cols: number): boolean => {
    if (index === word.length) return true;

    if (r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] !== word[index]) return false;
    const temp = board[r][c];

    board[r][c] = '🚪';
    const found = dfs(r + 1, c, index + 1, board, word, rows, cols) ||
        dfs(r - 1, c, index + 1, board, word, rows, cols) ||
        dfs(r, c + 1, index + 1, board, word, rows, cols) ||
        dfs(r, c - 1, index + 1, board, word, rows, cols);

    board[r][c] = temp;

    return found;
};

function exist(board: string[][], word: string): boolean {
    const rows = board.length;
    const cols = board[0].length;

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (dfs(r, c, 0, board, word, rows, cols)) return true;
        }
    }
    return false;
}
