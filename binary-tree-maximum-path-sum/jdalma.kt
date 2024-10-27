package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `binary-tree-maximum-path-sum` {

    /**
     * TC: O(n), SC: O(log n)
     */
    fun maxPathSum(root: TreeNode?): Int {
        if (root == null) return 0
        var max = root.`val`    // 부모 노드와 2개의 자식 노드의 합을 전역 변수로 갱신한다.

        fun dfs(node: TreeNode?): Int {
            if (node == null) return 0

            val left = max(dfs(node.left), 0)
            val right = max(dfs(node.right), 0)

            max = max(node.`val` + left + right, max)
            return node.`val` + max(left, right)    // 현재 노드와 2개의 자식 노드 중 최대의 값을 반환한다.
        }

        dfs(root)
        return max
    }

    @Test
    fun `이진 트리의 최대 경로 합을 반환한다`() {
        maxPathSum(TreeNode.of(-10,9,20,null,null,15,7)) shouldBe 42
        maxPathSum(TreeNode.of(1,9,20,null,null,15,7)) shouldBe 45
    }
}
