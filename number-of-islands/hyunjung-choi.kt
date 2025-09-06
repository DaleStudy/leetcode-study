/**
 * 시간복잡도: O(M × N)
 * 공간복잡도: O(M × N)
 */

class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        if (grid.isEmpty() || grid[0].isEmpty()) return 0

        val row = grid.size
        val column = grid[0].size
        var isIslandCount = 0

        for (i in 0 until row) {
            for (j in 0 until column) {
                if (grid[i][j] == '1') {
                    isIslandCount++
                    dfs(grid, i, j, row, column)
                }
            }
        }

        return isIslandCount
    }

    private fun dfs(grid: Array<CharArray>, i: Int, j: Int, row: Int, column: Int) {
        if (i < 0 || i >= row || j < 0 || j >= column || grid[i][j] != '1') {
            return
        }

        grid[i][j] = '0'

        dfs(grid, i - 1, j, row, column)
        dfs(grid, i + 1, j, row, column)
        dfs(grid, i, j - 1, row, column)
        dfs(grid, i, j + 1, row, column)
    }
}
