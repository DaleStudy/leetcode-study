var exist = function (board, word) {
    const rowLen = board.length, colLen = board[0].length;
    let visited = new Set(); // keep track of visited coordinates

    function dfs(row, col, idx) {
        if (idx === word.length) return true; // if idx equals word.length, it means the word exists
        if (row < 0 || col < 0 ||
            row >= rowLen || col >= colLen ||
            board[row][col] !== word[idx] ||
            visited.has(`${row}|${col}`)) return false; // possible cases that would return false


        // backtracking
        visited.add(`${row}|${col}`); 
        let result = dfs(row + 1, col, idx + 1) || // dfs on all 4 directions
            dfs(row - 1, col, idx + 1) ||
            dfs(row, col + 1, idx + 1) ||
            dfs(row, col - 1, idx + 1);
        visited.delete(`${row}|${col}`);

        return result;
    }

    for (let row = 0; row < rowLen; row++) {
        for (let col = 0; col < colLen; col++) {
            if(dfs(row, col, 0)) return true; // dfs for all coordinates
        }
    }

    return false;
};

// time - O(m * n * 4^w) traverse through the matrix (m * n) and run dfs on each of the possible paths (4^w) 4 being 4 directions 
// space - O(m * n  + w)
