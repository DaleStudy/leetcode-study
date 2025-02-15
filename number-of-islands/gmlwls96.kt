class Solution {
    // 시간 : O(N), 공간 O(N)
    fun numIslands(grid: Array<CharArray>): Int {
        val moveMap = arrayOf(
            intArrayOf(1, 0),
            intArrayOf(0, 1)
        )
        val queue = mutableListOf<IntArray>()
        val visitMap = Array(grid.size) {
            BooleanArray(grid[it].size)
        }
        var count = 0
        // 1. grid를 모두 조회
        for (y in grid.indices) {
            for (x in grid[y].indices) {
                // 2. grid[y][x]가 1이고 방문한적이 없으면 newLand로 인지하고 count를 올린다.
                if (grid[y][x] == '1' && !visitMap[y][x]) {
                    count++
                    queue.add(intArrayOf(y, x))
                }
                // 3. 인접해있는 land를 조회하기위해 queue를 이용하여 탐색하고, visitMap을 변경해준다.
                while (queue.isNotEmpty()) {
                    val newInfo = queue.removeFirst()
                    val newY = newInfo[0]
                    val newX = newInfo[1]
                    visitMap[newY][newX] = true
                    moveMap.forEach {
                        val nextY = newY + it[0]
                        val nextX = newX + it[1]
                        if (nextY < grid.size
                            && nextX < grid[nextY].size
                            && grid[nextY][nextX] == '1'
                            && !visitMap[nextY][nextX]
                        ) {
                            queue.add(intArrayOf(nextY, nextX))
                        }
                    }
                }
            }
        }
        return count
    }
}
