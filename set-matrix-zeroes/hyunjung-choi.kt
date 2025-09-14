/**
 * 시간복잡도: O(m × n)
 * 공간복잡도: O(1)
 */

class Solution {
    fun setZeroes(matrix: Array<IntArray>): Unit {
        val m = matrix.size
        val n = matrix[0].size

        var firstRowHasZero = false
        var firstColumnHasZero = false

        for (j in 0 until n) {
            if (matrix[0][j] == 0) {
                firstRowHasZero = true
                break
            }
        }

        for (i in 0 until m) {
            if (matrix[i][0] == 0) {
                firstColumnHasZero = true
                break
            }
        }

        for (i in 1 until m) {
            for (j in 1 until n) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                }
            }
        }

        for (i in 1 until m) {
            for (j in 1 until n) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0
                }
            }
        }

        for (j in 0 until n) {
            if (firstRowHasZero) {
                matrix[0][j] = 0
            }
        }

        for (i in 0 until m) {
            if (firstColumnHasZero) {
                matrix[i][0] = 0
            }
        }
    }
}
