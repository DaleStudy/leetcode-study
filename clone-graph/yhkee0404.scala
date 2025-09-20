import scala.collection.mutable.ListBuffer

/**
 * Definition for a Node.
 * class Node(var _value: Int) {
 *   var value: Int = _value
 *   var neighbors: List[Node] = List()
 * }
 */

object Solution {
    def cloneGraph(graph: Node): Node = {
        if (graph == null) {
            return null
        }
        val dp = Array.fill[Node](101)(null)
        cloneGraph(dp, graph)
    }
    def cloneGraph(dp: Array[Node], graph: Node): Node = {
        if (dp(graph.value) != null) {
            return dp(graph.value)
        }
        val u = Node(graph.value)
        dp(graph.value) = u
        val neighbors = ListBuffer[Node]()
        graph.neighbors
                .foreach {
                    neighbors += cloneGraph(dp, _)
                }
        u.neighbors ++= neighbors
        u
    }
}
