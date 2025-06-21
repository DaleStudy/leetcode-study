class Solution {
    // Time Complexity: O(n + e)
    // Space Complexity: O(n + e)
    // n : number of nodes
    // e : number of edges
    fun countComponents(n: Int, edges: Array<IntArray>): Int {
        val graph = Array(n) { mutableListOf<Int>() }
        for (edge in edges) { // make graph
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        }
        val visited = BooleanArray(n) // visited array
        var count = 0 // number of connected components

        for (i in 0 until n) {
            if (!visited[i]) {
                dfs(i, graph, visited)
                count++
            }
        }
        return count
    }

    fun dfs(node: Int, graph: Array<MutableList<Int>>, visited: BooleanArray) {
        visited[node] = true
        for (neighbor in graph[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, graph, visited)
            }
        }
    }
}
