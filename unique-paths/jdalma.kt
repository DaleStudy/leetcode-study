package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

/**
 * 0,0 에서 아래 또는 오른쪽으로만 이동 가능하다.
 */
class `unique-paths` {

    fun uniquePaths(row: Int, col: Int): Int {
        return if (row <= 1 || col <= 1) 1
        else usingArray(row, col)
    }

    /**
     * TC: O(n * m), SC: O(n * m)
     */
    private fun usingGrid(row: Int, col: Int): Int {
        val grid = Array(row) { IntArray(col) }
        (0 until row).forEach { grid[it][0] = 1 }
        (0 until col).forEach { grid[0][it] = 1 }

        for (i in 1 until row) {
            for (j in 1 until col) {
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
            }
        }

        return grid[row - 1][col - 1]
    }

    /**
     * 이전 라인의 배열만 기억하여도 되므로 공간 복잡도를 아래와 같이 줄일 수 있다.
     * TC: O(n * m), SC: O(m)
     */
    private fun usingArray(row: Int, col: Int): Int {
        var dp = IntArray(col)

        for (i in 0 until row) {
            val tmp = IntArray(col)
            for (j in 0 until col) {
                if (i == 0 && j == 0) tmp[j] = 1
                else if (j > 0) tmp[j] = dp[j] + tmp[j - 1]
                else tmp[j] = dp[j]
            }
            dp = tmp
        }

        return dp.last()
    }

    @Test
    fun `왼쪽 상단 모서리에서 오른쪽 상단 모서리로 도달할 수 있는 고유 경로의 수를 반환한다`() {
        uniquePaths(3, 7) shouldBe 28
        uniquePaths(3, 2) shouldBe 3
    }
}
