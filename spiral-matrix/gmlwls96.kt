class Solution {
    // 시간 : O(y*x), 공간 : O(1)
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        val result = mutableListOf<Int>()
        if (matrix.isEmpty() || matrix[0].isEmpty()) return result

        var top = 0
        var bottom = matrix.size - 1
        var left = 0
        var right = matrix[0].size - 1

        while (top <= bottom && left <= right) {
            for (i in left..right) result.add(matrix[top][i])
            top++
            for (i in top..bottom) result.add(matrix[i][right])
            right--
            if (top <= bottom) {
                for (i in right downTo left) result.add(matrix[bottom][i])
                bottom--
            }
            if (left <= right) {
                for (i in bottom downTo top) result.add(matrix[i][left])
                left++
            }
        }

        return result
    }
}
