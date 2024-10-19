package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `invert-binary-tree` {

    fun invertTree(root: TreeNode?): TreeNode? {
        if (root == null) return null

        return usingStack(root)
    }

    /**
     * TC: O(n), SC: O(n)
     */
    private fun usingDFS(node: TreeNode?): TreeNode? {
        if (node == null) return null

        val (left, right) = node.left to node.right
        node.left = usingDFS(right)
        node.right = usingDFS(left)

        return node
    }

    /**
     * TC: O(n), SC: O(n)
     */
    private fun usingStack(node: TreeNode): TreeNode {
        val stack= ArrayDeque<TreeNode>().apply {
            this.add(node)
        }

        while (stack.isNotEmpty()) {
            val now = stack.removeLast()
            val tmp = now.left
            now.left = now.right
            now.right = tmp

            now.left?.let { stack.add(it) }
            now.right?.let { stack.add(it) }
        }
        return node
    }

    @Test
    fun `전달된 노드의 하위 노드들의 반전된 값을 반환한다`() {
        val actual = TreeNode.of(4,2,7,1,3,6,9)
        val expect = TreeNode.of(4,7,2,9,6,3,1)
        invertTree(actual) shouldBe expect

        val actual1 = TreeNode.of(1,2)
        val expect1 = TreeNode.of(1,null,2)

        invertTree(actual1) shouldBe expect1
    }
}
