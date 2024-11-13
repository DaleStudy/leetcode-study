package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `binary-tree-level-order-traversal` {

    fun levelOrder(root: TreeNode?): List<List<Int>> {
        return if (root == null) emptyList()
        else usingDFS(root)
    }

    /**
     * TC: O(n), SC: O(n)
     */
    private fun usingBFS(root: TreeNode): List<List<Int>> {
        val queue = ArrayDeque<TreeNode>().apply {
            this.add(root)
        }

        val result = mutableListOf<List<Int>>()
        while (queue.isNotEmpty()) {
            val values = mutableListOf<Int>()
            repeat(queue.size) {
                val node = queue.removeFirst()
                values.add(node.`val`)
                node.left?.also { queue.add(it) }
                node.right?.also { queue.add(it) }
            }
            result.add(values)
        }

        return result
    }

    /**
     * TC: O(n), SC: O(n)
     */
    private fun usingDFS(root: TreeNode): List<List<Int>> {

        fun dfs(node: TreeNode, result: MutableList<MutableList<Int>>, depth: Int) {
            if (depth >= result.size) {
                result.add(mutableListOf())
            }
            result[depth].add(node.`val`)
            node.left?.also { dfs(it, result, depth + 1) }
            node.right?.also { dfs(it, result, depth + 1) }
        }

        return mutableListOf<MutableList<Int>>().apply {
            dfs(root, this, 0)
        }
    }

    @Test
    fun `트리 노드를 깊이 별로 반환한다`() {
        levelOrder(TreeNode.of(3,9,20,null,null,15,7)) shouldBe listOf(
            listOf(3),
            listOf(9,20),
            listOf(15,7)
        )
    }
}
