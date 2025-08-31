class Solution {
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        val visited = List(matrix.size) {MutableList(matrix.first().size) {false}} // T(n) = S(n) = O(n)
        val drcs = listOf(
            listOf(0, 1,),
            listOf(1, 0,),
            listOf(0, -1,),
            listOf(-1, 0,),
        )
        val ans = mutableListOf<Int>()
        search(ans, matrix, visited, drcs, 0, 0, 0, false)
        return ans
    }
}

fun search(ans: MutableList<Int>, matrix: Array<IntArray>, visited: List<MutableList<Boolean>>, drcs: List<List<Int>>, r: Int, c: Int, dir: Int, turned: Boolean) {
    val drc = drcs[dir]
    if (r == -1 || r == matrix.size || c == -1 || c == matrix.first().size || visited[r][c]) {
        if (turned) {
            return
        }
        val nDir = (dir + 1) % drcs.size
        val nDrc = drcs[nDir]
        search(ans, matrix, visited, drcs, r - drc[0] + nDrc[0], c - drc[1] + nDrc[1], nDir, true)
        return
    }
    visited[r][c] = true
    ans.add(matrix[r][c])
    search(ans, matrix, visited, drcs, r + drc[0], c + drc[1], dir, false)
}
