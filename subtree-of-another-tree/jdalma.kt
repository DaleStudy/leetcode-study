package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test

class `subtree-of-another-tree` {

    fun isSubtree(root: TreeNode?, subRoot: TreeNode?): Boolean {
        if (root == null) return false
        else if (isSame(root, subRoot)) return true

        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
    }

    private fun isSame(root: TreeNode?, subRoot: TreeNode?): Boolean {
        if (root == null && subRoot == null) return true
        if (root == null || subRoot == null) return false
        if (root.`val` != subRoot.`val`) return false

        return isSame(root.left, subRoot.left) && isSame(root.right, subRoot.right)
    }

    @Test
    fun `subRoot를 포함한다면 참을 반환한다`() {
        isSubtree(TreeNode.of(3,4,5,1,2,null,null,null,0), TreeNode.of(4,1,2)) shouldBe false
        isSubtree(TreeNode.of(3,4,5,1,2,null,null,null), TreeNode.of(4,1,2)) shouldBe true
    }
}
