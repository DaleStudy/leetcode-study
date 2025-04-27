/**
 * [Problem]: [79] Word Search
 *
 * (https://leetcode.com/problems/word-search/description/)
 */

function exist(board: string[][], word: string): boolean {
    //시간복잡도 O(m * n * 4^w)
    //공간복잡도 O(w)
    function dfsChangingBoard(board: string[][], word: string): boolean {
        const rows = board.length;
        const cols = board[0].length;

        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                if (dfs(i, j, 0)) return true;
            }
        }

        return false;

        function dfs(i: number, j: number, k: number): boolean {
            if (k === word.length) return true;

            if (i < 0 || j < 0) return false;
            if (i >= rows || j >= cols) return false;
            if (board[i][j] !== word[k]) return false;

            const temp = board[i][j];
            board[i][j] = "";

            const result =
                dfs(i + 1, j, k + 1) ||
                dfs(i - 1, j, k + 1) ||
                dfs(i, j + 1, k + 1) ||
                dfs(i, j - 1, k + 1);

            board[i][j] = temp;
            return result;
        }
    }

    //시간복잡도 O(m * n * 4^w)
    //공간복잡도 O(w)
    function dfsMaintainingBoard(board: string[][], word: string): boolean {
        const rows = board.length;
        const cols = board[0].length;

        // array보다 Set<string>이 더 효율적
        // Set.has: O(1)  / Array.includes: O(n)
        const passed = new Set<string>();

        for (let i = 0; i < rows; i++) {
            for (let j = 0; j < cols; j++) {
                if (dfs(i, j, 0)) return true;
            }
        }

        return false;

        function dfs(i: number, j: number, k: number): boolean {
            if (k === word.length) return true;

            if (i < 0 || j < 0) return false;
            if (i >= rows || j >= cols) return false;
            if (board[i][j] !== word[k]) return false;
            if (passed.has(`${i},${j}`)) return false;

            passed.add(`${i},${j}`);

            const result =
                dfs(i + 1, j, k + 1) ||
                dfs(i - 1, j, k + 1) ||
                dfs(i, j + 1, k + 1) ||
                dfs(i, j - 1, k + 1);

            passed.delete(`${i},${j}`);
            return result;
        }
    }

    return dfsMaintainingBoard(board, word);
}
