package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `pacific-atlantic-water-flow` {

    private val dirs = listOf(
        intArrayOf(0, 1),
        intArrayOf(0, -1),
        intArrayOf(1, 0),
        intArrayOf(-1, 0)
    )

    /**
     * TC: O(n * m), SC: O(n * m)
     */
    fun pacificAtlantic(heights: Array<IntArray>): List<List<Int>> {
        val (row, col) = heights.size to heights.first().size
        val pacific = Array(row) { BooleanArray(col) }
        val atlantic = Array(row) { BooleanArray(col) }

        for (index in 0 until row) {
            dfs(heights, pacific, Int.MIN_VALUE, index, 0)
            dfs(heights, atlantic, Int.MIN_VALUE, index, col - 1)
        }

        for (index in 0 until col) {
            dfs(heights, pacific, Int.MIN_VALUE, 0, index)
            dfs(heights, atlantic, Int.MIN_VALUE, row - 1, index)
        }

        val result = mutableListOf<List<Int>>()
        for (i in 0 until row) {
            for (j in 0 until col) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.add(listOf(i, j))
                }
            }
        }
        return result
    }

    private fun dfs(heights: Array<IntArray>, visited: Array<BooleanArray>, height: Int, r: Int, c: Int) {
        val (row, col) = heights.size to heights.first().size
        if (r < 0 || r >= row || c < 0 || c >= col || visited[r][c] || heights[r][c] < height)
            return

        visited[r][c] = true
        for (dir in dirs) {
            dfs(heights, visited, heights[r][c], r + dir[0], c + dir[1])
        }
    }

    @Test
    fun `태평양과 대서양에 모두 흐를 수 있는 셀의 위치를 반환하라`() {
        pacificAtlantic(
            arrayOf(
                intArrayOf(1,2,2,3,5),
                intArrayOf(3,2,3,4,4),
                intArrayOf(2,4,5,3,1),
                intArrayOf(6,7,1,4,5),
                intArrayOf(5,1,1,2,4)
            )
        ) shouldBe arrayOf(
            intArrayOf(0,4),
            intArrayOf(1,3),
            intArrayOf(1,4),
            intArrayOf(2,2),
            intArrayOf(3,0),
            intArrayOf(3,1),
            intArrayOf(4,0)
        )
    }
}
