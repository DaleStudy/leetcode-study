class Solution {

    private val dx = intArrayOf(-1, 1, 0, 0)
    private val dy = intArrayOf(0, 0, -1, 1)

    fun exist(board: Array<CharArray>, word: String): Boolean {
        val rows = board.size
        val cols = board[0].size
        val visited = Array(rows) { BooleanArray(cols) }

        val starts = mutableListOf<Pair<Int, Int>>()
        for (i in 0 until rows) {
            for (j in 0 until cols) {
                if (board[i][j] == word[0]) starts.add(i to j)
            }
        }

        if (word.length == 1) return starts.isNotEmpty()

        var flag = false

        fun dfs(start: Pair<Int, Int>, index: Int) {
            if (flag) return
            if (index == word.length - 1) {
                flag = true
                return
            }

            for (i in 0 until 4) {
                val nx = start.first + dx[i]
                val ny = start.second + dy[i]

                if (nx < 0 || nx >= rows) continue
                if (ny < 0 || ny >= cols) continue
                if (visited[nx][ny]) continue
                if (word[index + 1] != board[nx][ny]) continue

                visited[nx][ny] = true
                dfs(Pair(nx, ny), index + 1)
                visited[nx][ny] = false
            }
        }

        for (start in starts) {
            visited[start.first][start.second] = true
            dfs(start, 0)
            visited[start.first][start.second] = false
            if (flag) return true
        }

        return false
    }
}
