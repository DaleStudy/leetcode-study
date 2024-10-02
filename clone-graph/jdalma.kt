package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import java.lang.RuntimeException
import java.util.ArrayDeque
import java.util.Queue

class `clone-graph` {

    data class Node(var `val`: Int) {
        var neighbors: ArrayList<Node?> = ArrayList()
    }

    fun cloneGraph(node: Node?): Node? {
        if (node == null) return null

        return usingBFS(node)
    }

    /**
     * TC: O(n), SC: O(n)
     */
    private fun usingDFS(node: Node): Node {

        fun dfs(node: Node, nodes: MutableMap<Int, Node>): Node {
            nodes[node.`val`]?.let {
                return it
            }
            val copy = Node(node.`val`)
            nodes[node.`val`] = copy

            for (near in node.neighbors.filterNotNull()) {
                copy.neighbors.add(dfs(near, nodes))
            }

            return copy
        }
        return dfs(node, mutableMapOf())
    }

    /**
     * TC: O(n), SC: O(n)
     */
    private fun usingBFS(node: Node): Node {
        val nodes = mutableMapOf<Int, Node>().apply {
            this[node.`val`] = Node(node.`val`)
        }
        val queue: Queue<Node> = ArrayDeque<Node>().apply {
            this.offer(node)
        }

        while (queue.isNotEmpty()) {
            val now = queue.poll()
            val copy = nodes[now.`val`] ?: throw RuntimeException()
            for (near in now.neighbors.filterNotNull()) {
                if (!nodes.containsKey(near.`val`)) {
                    nodes[near.`val`] = Node(near.`val`)
                    queue.add(near)
                }
                copy.neighbors.add(nodes[near.`val`])
            }
        }
        return nodes[node.`val`] ?: Node(node.`val`)
    }

    private fun fixture(): Node {
        val one = Node(1)
        val two = Node(2)
        val three = Node(3)
        val four = Node(4)

        one.neighbors.add(two)
        one.neighbors.add(four)
        two.neighbors.add(one)
        two.neighbors.add(three)
        three.neighbors.add(two)
        three.neighbors.add(four)
        four.neighbors.add(one)
        four.neighbors.add(three)

        return one
    }

    @Test
    fun `입력받은 노드의 깊은 복사본을 반환한다`() {
        val actualNode = fixture()
        val expectNode = cloneGraph(actualNode)
        actualNode shouldBe expectNode

        actualNode.`val` = 9999
        expectNode!!.`val` shouldBe 1
    }
}
