val _DRCS = listOf(
    listOf(0, -1),
    listOf(0, 1),
    listOf(-1, 0),
    listOf(1, 0),
)

class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        val offset = 'A'.code
        val invertedIndex = List('z'.code - offset + 1) {mutableListOf<List<Int>>()}
        board.withIndex()
                .forEach { row ->
                    row.value
                            .withIndex()
                            .forEach {
                                invertedIndex[it.value.toInt() - offset].add(listOf(row.index, it.index))
                            }
                }
        val freq = MutableList(invertedIndex.size) {0}
        word.map {it.toInt() - offset}
                .forEach {
                    freq[it]++
                }
        if ((0 until freq.size).any {freq[it] > invertedIndex[it].size}) {
            return false
        }
        val target = if (invertedIndex[word.first().toInt() - offset].size <= invertedIndex[word.last().toInt() - offset].size) word
        else word.reversed()
        val stack = invertedIndex[target.first().toInt() - offset].map {
                    mutableListOf(it.first(), it.last(), 0, 1)
                }.toMutableList()
        val visited = MutableList(board.size) {MutableList(board.first().size) {false}}
        while (! stack.isEmpty()) {
            val u = stack.last()
            if (u[2] == 4) {
                visited[u[0]][u[1]] = false
                stack.removeLast()
                continue
            }
            if (u[2] == 0) {
                if (u[3] == target.length) {
                    return true
                }
                visited[u[0]][u[1]] = true
            }
            val drc = _DRCS[u[2]]
            u[2]++
            val v = mutableListOf(u[0] + drc[0], u[1] + drc[1], 0, u[3] + 1)
            if (v[0] == -1 || v[0] == board.size || v[1] == -1 || v[1] == board.first().size
                    || visited[v[0]][v[1]] || board[v[0]][v[1]] != target[u[3]]) {
                continue
            }
            stack.add(v)
        }
        return false
    }
}
