package leetcode_study

/**
 * n: rowSize, m: colSize
 * 시간복잡도 : O(n*m)
 * - 전체 그리드를 한번씩만 방문하므로, 시간복잡도는 O(n*m) 과 같습니다.
 * 공간복잡도 : O(n*m)
 * - 방문이력에 대해 visited 를 저장하므로, 시간복잡도는 O(n*m) 과 같습니다.
 * */
class NumberOfIsland {
    val directions = listOf(
        Pair(-1, 0),
        Pair(1, 0),
        Pair(0, -1),
        Pair(0, 1)
    )
    var rowSize = 0
    var colSize = 0
    var visited: Array<BooleanArray>? = null

    fun numIslands(grid: Array<CharArray>): Int {
        rowSize = grid.size
        colSize = grid[0].size
        visited = Array(rowSize) { BooleanArray(colSize) }

        var islandCnt = 0

        for (i in 0 until rowSize) {
            for (j in 0 until colSize) {
                if (grid[i][j] == '1' && !visited!![i][j]) {
                    dfs(i, j, grid)
                    islandCnt += 1
                }
            }
        }

        return islandCnt
    }

    fun dfs(r: Int, c: Int, grid: Array<CharArray>) {
        visited!![r][c] = true

        for ((dr, dc) in directions) {
            val (nr, nc) = Pair(r + dr, c + dc)
            if (isValid(nr, nc, grid)) {
                dfs(nr, nc, grid)
            }
        }
    }

    private fun isValid(r: Int, c: Int, grid: Array<CharArray>): Boolean {
        return r in 0 until rowSize &&
                c in 0 until colSize &&
                grid[r][c] == '1' &&
                !visited!![r][c]
    }
}