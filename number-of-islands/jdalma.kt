package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `number-of-islands` {

    private data class Position(
        val x: Int,
        val y: Int
    ) {

        operator fun plus(other: Position) = Position(this.x + other.x, this.y + other.y)

        fun isNotOutOfIndexed(board: Array<CharArray>) =
            this.x < board.size && this.x >= 0 && this.y < board[0].size &&  this.y >= 0

        companion object {
            val MOVES: List<Position> = listOf(
                Position(-1, 0),
                Position(0, 1),
                Position(1, 0),
                Position(0, -1),
            )
        }
    }

    /**
     * BFS를 사용한 탐색
     * TC: O(n * m), SC: O(n * m)
     */
    fun numIslands(grid: Array<CharArray>): Int {
        val (row, col) = grid.size to grid.first().size
        val visited = Array(row) { BooleanArray(col) }
        var result = 0

        for (x in 0 until row) {
            for (y in 0 until col) {
                if (!visited[x][y] && grid[x][y] == '1') {
                    visited[x][y] = true
                    bfs(x, y, grid, visited)
                    result++
                }
            }
        }
        return result
    }

    private fun bfs(x: Int, y: Int, grid: Array<CharArray>, visited: Array<BooleanArray>) {
        val queue = ArrayDeque<Position>().apply {
            this.add(Position(x, y))
        }

        while (queue.isNotEmpty()) {
            val now = queue.removeFirst()
            for (move in Position.MOVES) {
                val moved = now + move
                if (moved.isNotOutOfIndexed(grid) && grid[moved.x][moved.y] == '1' && !visited[moved.x][moved.y]) {
                    visited[moved.x][moved.y] = true
                    queue.add(moved)
                }
            }
        }
    }


    @Test
    fun `문자 이차원배열을 입력받으면 1로 이루어진 영역의 수를 반환한다`() {
        numIslands(arrayOf(
            charArrayOf('1','1','1','1','0'),
            charArrayOf('1','1','0','1','0'),
            charArrayOf('1','1','0','0','0'),
            charArrayOf('0','0','0','0','0')
        )) shouldBe 1

        numIslands(arrayOf(
            charArrayOf('1','1','0','0','0'),
            charArrayOf('1','1','0','0','0'),
            charArrayOf('0','0','1','0','0'),
            charArrayOf('0','0','0','1','1')
        )) shouldBe 3
    }
}
