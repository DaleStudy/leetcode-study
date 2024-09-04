package leetcode_study

import io.kotest.matchers.shouldBe
import leetcode_study.`word-search`.Position.Companion.MOVES
import org.junit.jupiter.api.Test

class `word-search` {

    /**
     * 격자에 존재하는 문자를 사용하여 word 를 만들 수 있는지 확인하기 위해 DFS를 통한 visited 배열 백트래킹을 사용하여 해결
     * TC: O(너비 * 높이 * 4^word), SC: O(너비 * 높이 * 4^word)
     */
    fun exist(board: Array<CharArray>, word: String): Boolean {
        return usingBacktracking(board, word)
    }

    private fun usingBacktracking(board: Array<CharArray>, word: String): Boolean {
        fun dfs(board: Array<CharArray>, visited: Array<BooleanArray>, word: String, position: Position, index: Int): Boolean {
            if (index == word.length) return true
            for (move in MOVES) {
                val next = position + move
                if (next.isNotOutOfIndexed(board) && !visited[next.x][next.y] && board[next.x][next.y] == word[index]) {
                    visited[next.x][next.y] = true
                    if (dfs(board, visited, word, next, index + 1)) return true
                    visited[next.x][next.y] = false
                }
            }
            return false
        }

        val visited = Array(board.size) {
            BooleanArray(board[0].size)
        }

        for (x in board.indices) {
            for (y in board[x].indices) {
                visited[x][y] = true
                if (board[x][y] == word[0] && dfs(board, visited, word, Position(x,y), 1)) {
                    return true
                }
                visited[x][y] = false
            }
        }
        return false
    }

    @Test
    fun `문자로 구성된 2차원 배열에서 word 문자열 존재 유무를 반환한다`() {
        exist(arrayOf(
            charArrayOf('A','B','C','E'),
            charArrayOf('S','F','C','S'),
            charArrayOf('A','D','E','E')
        ), "ABCCED") shouldBe true
        exist(arrayOf(
            charArrayOf('A','B','C','E'),
            charArrayOf('S','F','C','S'),
            charArrayOf('A','D','E','E')
        ), "SEE") shouldBe true
        exist(arrayOf(
            charArrayOf('A','B','C','E'),
            charArrayOf('S','F','C','S'),
            charArrayOf('A','D','E','E')
        ), "SES") shouldBe false
        exist(arrayOf(
            charArrayOf('A','B','C','E'),
            charArrayOf('S','F','E','S'),
            charArrayOf('A','D','E','E')
        ), "ABCESEEEFS") shouldBe true
        exist(arrayOf(
            charArrayOf('C','A','A'),
            charArrayOf('A','A','A'),
            charArrayOf('B','C','D')
        ), "AAB") shouldBe true
    }

    data class Position(
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
}
