package leetcode_study

import io.kotest.matchers.shouldBe
import org.junit.jupiter.api.Test
import kotlin.math.max

class `maximum-depth-of-binary-tree` {

    /**
     * 이진 트리이기에 스택의 깊이가 차지하는 공간 복잡도는 log일 것
     * TC: O(n), SC: O(log n)
     */
    fun maxDepth(root: TreeNode?): Int {
        return if (root == null) 0
        else max(maxDepth(root.left) + 1, maxDepth(root.right) + 1)
    }

    @Test
    fun `노드의 최대 깊이를 반환한다`() {
        maxDepth(TreeNode.of(3,9,20,null,null,15,7)) shouldBe 3
    }
}
