class Solution {
    // 시간 : O(mn) 공간 : O(m+n)
    // 변경해야되는 position 찾아 yList, xList에 각각 y,x값을 담되 set을 이용하여 중복을 제거한다.
    // yList, xList를 조회하며 matrix를 변경해준다.
    fun setZeroes(matrix: Array<IntArray>): Unit {
        val yList = mutableSetOf<Int>()
        val xList = mutableSetOf<Int>()
        for (y in 0 until matrix.size) {
            for (x in 0 until matrix[y].size) {
                if (matrix[y][x] == 0) {
                    yList.add(y)
                    xList.add(x)
                }
            }
        }
        yList.forEach { y ->
            for (x in 0 until matrix[y].size) {
                matrix[y][x] = 0
            }
        }
        xList.forEach { x ->
            for (y in 0 until matrix.size) {
                matrix[y][x] = 0
            }
        }
    }
}
