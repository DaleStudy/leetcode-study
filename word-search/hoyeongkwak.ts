function exist(board: string[][], word: string): boolean {
    /*
    O(m * n)
    O(m * n)
    */
    const rowsLen = board.length
    const colsLen = board[0].length 
    const direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    const visited = Array(rowsLen).fill(0).map(() => Array(colsLen).fill(false))
    const dfs = (row: number, col: number, idx: number): boolean => {
        if (idx === word.length)
            return true
        if (row < 0 || row >= rowsLen || col < 0 || 
        col >= colsLen || board[row][col] !== word[idx] || visited[row][col])
            return false    
        visited[row][col] = true
        if (idx === word.length - 1) return true
        for (const [dx, dy] of direction) {
            const newRow = row + dx
            const newCol = col + dy

            if (newRow >= 0 && newRow < rowsLen && newCol >= 0 && newCol < colsLen && !visited[newRow][newCol] && board[newRow][newCol] === word[idx + 1]) {
                if (dfs(newRow, newCol, idx + 1)) {
                    return true
                }
            }
        }
        visited[row][col] = false
        return false
    }

    for (let r = 0; r < rowsLen; r++) {
        for(let c = 0; c < colsLen; c++) {
            if (board[r][c] === word[0] && dfs(r, c, 0)) {
                return true
            }
        }
    }
    return false
};
