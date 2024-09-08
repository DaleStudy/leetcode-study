
// m은 board의 행 수, n은 board의 열 수, 4(상하좌우), l(word)

// 시간복잡도: O(m * n * 4L)
// 공간복잡도: O(m * n)

const d_row = [1, -1, 0, 0]
const d_col = [0, 0, -1, 1]


const isMoveBoard = (new_row, new_col, board) => {
    return new_row >= 0 && new_row < board.length && new_col >= 0 && new_col < board[0].length
}


/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    let result = false

    const visited = Array.from({length: board.length} , () => Array.from({length: board[0].length}).fill(false))

    const dfs = (strs, row, col, count) => {

        if (strs[count] !== word[count]) return
        if (strs.length > word.length) return

        if (strs === word)  {
            result = true
            return
        }

        for (let i = 0 ; i < d_row.length; i++) {
            const new_row = row + d_row[i]
            const new_col = col + d_col[i]

            if (isMoveBoard(new_row, new_col, board) && visited[new_row][new_col] !== true){
                visited[new_row][new_col] = true
                dfs(strs+board[new_row][new_col], new_row, new_col, count+1)
                visited[new_row][new_col] = false
            }
        }



    }


    for (let row = 0 ; row < board.length ; row++) {
        for (let col = 0 ; col < board[0].length ; col++) {
            visited[row][col] = true
            dfs(board[row][col], row, col , 0)
            visited[row][col] = false
        }
    }


    return result
};

console.log(exist([["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]], "ABCCED"))
console.log(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
console.log(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

