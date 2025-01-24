class Solution {
    // 시간 : O(m*n) 공간 : O(m*n)
    // dp 알고리즘. pathMap[y][x]로 올수 있는 경로의 수는
    // 위쪽(pathMap[y - 1][x]) + 왼쪽( pathMap[y][x - 1]) 경로의 수의 합이다.
    fun uniquePaths(m: Int, n: Int): Int {
        val pathMap = Array(m) { y ->
            IntArray(n) { x ->
                if (y == 0 || x == 0) {
                    1
                } else {
                    0
                }
            }
        }
        for (y in 1 until m) {
            for (x in 1 until n) {
                pathMap[y][x] = pathMap[y - 1][x] + pathMap[y][x - 1]
            }
        }

        return pathMap[m - 1][n - 1]
    }
}
