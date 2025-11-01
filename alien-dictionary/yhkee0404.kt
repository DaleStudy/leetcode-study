class Solution {
    /**
     * @param words: a list of words
     * @return: a string which is correct order
     */
    fun alienOrder(words: Array<String>): String {
        // Write your code here
        val adj = List<MutableList<Int>>('z'.code - 'a'.code + 1) {mutableListOf()}
        for (i in 1 until words.size) {
            var j = 0
            while (j != words[i - 1].length && j != words[i].length && words[i - 1][j] == words[i][j]) {
                j++
            }
            if (j == words[i - 1].length) {
                continue
            }
            if (j == words[i].length) {
                return ""
            }
            adj[words[i - 1][j].code - 'a'.code].add(words[i][j].code - 'a'.code)
        }
        val visited = MutableList(adj.size) {false}
        words.forEach {
                    it.map { it.code - 'a'.code }
                            .forEach { visited[it] = true }
                }
        val inDegrees = MutableList(adj.size) {0} // Kahn T(V, E) = S(V, E) = O(V + E)
        adj.forEach {
                    it.forEach { inDegrees[it]++ }
                }
        val ans = mutableListOf<Int>()
        val stack = mutableListOf<Int>()
        (0 until adj.size).filter { visited[it] && inDegrees[it] == 0 }
                .forEach {
                    stack.add(it)
                    ans.add(it)
                }
        while (! stack.isEmpty()) {
            val u = stack.removeLast()
            adj[u].forEach {
                        if (--inDegrees[it] == 0) {
                            stack.add(it)
                            ans.add(it)
                        }
                    }
        }
        if ((0 until adj.size).any { visited[it] && inDegrees[it] != 0 }) {
            return ""
        }
        return ans.map { (it + 'a'.code).toChar() }
                .joinToString("")
        /*val decoder = MutableList(adj.size) {0}
        (0 until ans.size).forEach { decoder[ans[it]] = it }
        val decoded = words.map {
                    it.map { (decoder[it.code - 'a'.code] + 'a'.code).toChar() }
                            .joinToString("")
                }
        val sortedWords = decoded.sorted()
        return if (decoded == sortedWords) ans.map { (it + 'a'.code).toChar() }
                        .joinToString("")
            else ""*/
    }
}
