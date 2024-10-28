package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `same-tree` {

    fun isSameTree(p: TreeNode?, q: TreeNode?): Boolean {
        return if (p == null && q == null) {
            true
        } else if (p == null || q == null || p.`val` != q.`val`) {
            false
        } else {
            isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
        }
    }

    @Test
    fun `두 개의 트리의 동등성을 반환한다`() {
        isSameTree(
            TreeNode.of(1,1,2),
            TreeNode.of(1,1,2)
        ) shouldBe true

        isSameTree(
            TreeNode.of(1,1,2),
            TreeNode.of(1,1,2,3)
        ) shouldBe false

        isSameTree(
            TreeNode.of(1,1,2),
            TreeNode.of(1,1,3)
        ) shouldBe false
    }
}
