class Solution {
    /**
     * @param n: the number of vertices
     * @param edges: the edges of undirected graph
     * @return: the number of connected components
     */
    fun countComponents(n: Int, edges: Array<IntArray>): Int {
        // write your code here
        val adj = List(n) {mutableListOf<Int>()}
        edges.forEach {
                    adj[it[0]].add(it[1])
                    adj[it[1]].add(it[0])
                }
        val visited = MutableList(n) {false} // T(V, E) = S(V, E) = O(V + E)
        val stack = mutableListOf<Int>()
        var ans = 0
        for (i in 0 until n) {
            if (visited[i]) {
                continue
            }
            ans++
            visited[i] = true
            stack.add(i)
            while (! stack.isEmpty()) {
                val u = stack.removeLast()
                adj[u].filter {! visited[it]}
                        .forEach {
                            visited[it] = true
                            stack.add(it)
                        }
            }
        }
        return ans
    }
}
