package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max
import kotlin.math.min

class `lowest-common-ancestor-of-a-binary-search-tree` {

    /**
     * TC: O(log n), SC: O(1)
     */
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode?, q: TreeNode?): TreeNode? {
        if (p == null || q == null) return null

        var node = root
        val max = max(p.`val`, q.`val`)
        val min = min(p.`val`, q.`val`)

        while (node != null) {
            node = if (node.`val` > max) {
                node.left
            } else if (node.`val` < min) {
                node.right
            } else {
                return node
            }
        }
        return null
    }

    @Test
    fun `가장 낮은 값의 공통 조상을 반환한다`() {
        lowestCommonAncestor(
            TreeNode.of(6,2,8,0,4,7,9,null,null,3,5),
            TreeNode(2),
            TreeNode(8)
        )!!.`val` shouldBe 6
    }
}
