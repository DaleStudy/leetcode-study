package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `set-matrix-zeroes` {

    private data class Position(
        val x: Int,
        val y: Int
    )

    fun setZeroes(matrix: Array<IntArray>): Unit {
        usingFlag(matrix)
    }

    /**
     * 0으로 변경해야 할 열과 행을 Set에 담아 처리한다.
     * TC: O(n * m) SC: O(n + m)
     */
    private fun usingSet(matrix: Array<IntArray>) {
        val zeroRows = mutableSetOf<Int>()
        val zeroCols = mutableSetOf<Int>()
        for (i in matrix.indices) {
            for (j in matrix.first().indices) {
                if (matrix[i][j] == 0) {
                    zeroRows.add(i)
                    zeroCols.add(j)
                }
            }
        }

        for (row in zeroRows) {
            for (col in matrix.first().indices) {
                matrix[row][col] = 0
            }
        }

        for (col in zeroCols) {
            for (row in matrix.indices) {
                matrix[row][col] = 0
            }
        }
    }

    /**
     * 0으로 변경해야 할 열과 행을 matrix 0번째 행과 0번째 열 그리고 두 개의 flag로 처리하여 공간복잡도를 개선한다.
     * TC: O(n * m) SC: O(1)
     */
    private fun usingFlag(matrix: Array<IntArray>) {
        var (rowFlag, colFlag) = false to false
        for (i in matrix.indices) {
            for (j in matrix.first().indices) {
                if (matrix[i][j] == 0) {
                    if (i == 0) rowFlag = true
                    if (j == 0) colFlag = true
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                }
            }
        }

        for (i in 1 until matrix.size) {
            for (j in 1 until matrix.first().size) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0
                }
            }
        }

        if (rowFlag) {
            for (i in matrix.first().indices) {
                matrix[0][i] = 0
            }
        }

        if (colFlag) {
            for (element in matrix) {
                element[0] = 0
            }
        }
    }

    @Test
    fun `원소가 0이라면 해당 행과 열을 모두 0으로 수정한다`() {
        val actual1 = arrayOf(
            intArrayOf(1,1,1),
            intArrayOf(1,0,1),
            intArrayOf(1,1,1)
        )
        setZeroes(actual1)
        actual1 shouldBe arrayOf(
            intArrayOf(1,0,1),
            intArrayOf(0,0,0),
            intArrayOf(1,0,1)
        )

        val actual2 = arrayOf(
            intArrayOf(0,1,2,0),
            intArrayOf(3,4,5,2),
            intArrayOf(1,3,1,5)
        )
        setZeroes(actual2)
        actual2 shouldBe arrayOf(
            intArrayOf(0,0,0,0),
            intArrayOf(0,4,5,0),
            intArrayOf(0,3,1,0)
        )
    }
}
