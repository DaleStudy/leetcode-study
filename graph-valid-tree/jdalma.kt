package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `graph-valid-tree` {

    /**
     * TC: O(n), SC: O(n)
     */
    fun validTree(nodeSize: Int, edges: Array<IntArray>): Boolean {
        if (nodeSize - 1 != edges.size) {
            return false
        }

        val visited = mutableSetOf<Int>()
        val adj = List(nodeSize) { mutableListOf<Int>() }
        for (e in edges) {
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])
        }

        val queue = ArrayDeque<Int>().apply {
            this.add(0)
        }

        while (queue.isNotEmpty()) {
            val now = queue.removeFirst()
            visited.add(now)
            for (next in adj[now]) {
                if (!visited.contains(next)) {
                    queue.add(next)
                }
            }
        }

        return nodeSize == visited.size
    }

    @Test
    fun `노드가 트리의 조건을 만족하는지 여부를 반환한다`() {
        validTree(5,
            arrayOf(
                intArrayOf(0,1),
                intArrayOf(0,2),
                intArrayOf(0,3),
                intArrayOf(1,4)
            )
        ) shouldBe true

        validTree(5,
            arrayOf(
                intArrayOf(0,1),
                intArrayOf(0,2),
                intArrayOf(0,3),
                intArrayOf(1,4),
                intArrayOf(2,3),
            )
        ) shouldBe false
    }
}
