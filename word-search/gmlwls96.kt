class Solution {

    // 풀이 : dfs
    // 시간 :O(m * n * 4^w), 공간 :O(m * n + w)
    val movePos = arrayOf(
        intArrayOf(-1, 0),
        intArrayOf(0, -1),
        intArrayOf(1, 0),
        intArrayOf(0, 1)
    )

    fun exist(board: Array<CharArray>, word: String): Boolean {
        for (y in board.indices) {
            for (x in board[y].indices) {
                if (existDfs(
                        board,
                        Array(board.size) { BooleanArray(board[it].size) },
                        word,
                        "",
                        y,
                        x
                    )
                ) {
                    return true
                }
            }
        }
        return false
    }

    private fun existDfs(
        board: Array<CharArray>,
        visit: Array<BooleanArray>,
        findWord: String,
        currentWord: String,
        y: Int,
        x: Int
    ): Boolean {
        if (findWord == currentWord) return true
        val findChar = findWord[currentWord.length]
        if (board[y][x] == findChar) {
            val newWord = currentWord + board[y][x]
            visit[y][x] = true
            for (pos in movePos) {
                val newY = y + pos[0]
                val newX = x + pos[1]
                if (newY >= 0 && newX >= 0
                    && newY < board.size
                    && newX < board[newY].size
                    && !visit[newY][newX]
                    && existDfs(
                        board = board,
                        visit = visit,
                        findWord = findWord,
                        currentWord = newWord,
                        y = newY,
                        x = newX
                    )
                ) {
                    return true
                }
            }
            visit[y][x] = false
        }
        return false
    }
}
