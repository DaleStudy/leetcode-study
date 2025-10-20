class Solution {
    /**
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    fun validTree(n: Int, edges: Array<IntArray>): Boolean {
        // write your code here
        val adj = List(n) {mutableListOf<Int>()} // S(V, E) = O(V + E)
        edges.forEach {
                    adj[it[0]].add(it[1])
                    adj[it[1]].add(it[0])
                }
        var t = 0
        val tortoiseStack = mutableListOf<MutableList<Int>>(mutableListOf(0, 0, -1))
        val hareStack = mutableListOf<MutableList<Int>>(mutableListOf(0, 0, -1))
        var tortoise = listOf(-1)
        while (! hareStack.isEmpty()) { // T(V, E) = O(V + E)
            val hare = hareStack.last()
            if (hare[1] == adj[hare[0]].size) {
                hareStack.removeLast()
            } else if (adj[hare[0]][hare[1]] != hare[2]) {
                hareStack.add(mutableListOf(adj[hare[0]][hare[1]], 0, hare[0]))
            }
            if (hare[1]++ != 0) {
                continue
            }
            if ((t++ and 1) == 1) {
                while (! tortoiseStack.isEmpty()) {
                    tortoise = tortoiseStack.last()
                    if (tortoise[1] == adj[tortoise[0]].size) {
                        tortoiseStack.removeLast()
                    } else if (adj[tortoise[0]][tortoise[1]] != tortoise[2]) {
                        tortoiseStack.add(mutableListOf(adj[tortoise[0]][tortoise[1]], 0, tortoise[0]))
                    }
                    if (tortoise[1]++ != 0) {
                        continue
                    }
                    break
                }
            }
            if (hare[0] == tortoise[0]) {
                return false
            }
        }
        return t == n
    }
}
