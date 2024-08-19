package leetcode_study

import io.kotest.matchers.equals.shouldBeEqual
import org.junit.jupiter.api.Test

class `construct-binary-tree-from-preorder-and-inorder-traversal` {

    /**
     * preorder : 현재(부모) 노드부터 왼쪽 자식 노드, 오른쪽 자식 노드
     * inorder : 왼쪽 자식 노드 부터 부모 노드, 오른쪽 자식 노드
     */
    fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
        val inorderIndices = inorder.withIndex().associate { it.value to it.index }
        return traversal(preorder, inorder, inorderIndices)
    }

    /**
     * preorder에서 조회한 부모 노드의 값은 inorder의 중간에 위치한다.
     * 그 중간 위치 기준으로 왼쪽 노드, 오른쪽 노드로 분리하여 재귀적으로 탐색할 수 있다.
     */
    private fun traversal(
        preorder: IntArray, inorder: IntArray, inorderIndices: Map<Int, Int>,
        preStart: Int = 0, inStart: Int = 0, inEnd: Int = inorder.size - 1
    ): TreeNode? {
        if (preStart > preorder.size - 1 || inStart > inEnd) {
            println("preStart: $preStart, inStart: $inStart, inEnd: $inEnd --- return null")
            return null
        }
        val value = preorder[preStart]
        val rootIndexInInorder = inorderIndices[value]!!

        println("value: $value, preStart: $preStart, rootIndexInInorder: $rootIndexInInorder, inStart: $inStart, inEnd: $inEnd")
        return TreeNode(value).apply {
            this.left = traversal(
                preorder, inorder, inorderIndices,
                preStart + 1, inStart, rootIndexInInorder - 1
            )
            this.right = traversal(
                preorder, inorder, inorderIndices,
                preStart + rootIndexInInorder - inStart + 1, rootIndexInInorder + 1,  inEnd
            )
        }
    }

    @Test
    fun `전위 순회, 중위 순회 순서의 정수 배열을 기준으로 이진트리를 생성하여 반환한다`() {
        val actual = buildTree(intArrayOf(3,9,20,15,7), intArrayOf(9,3,15,20,7))!!
        val expect = TreeNode.of(3,9,20,null,null,15,7)!!

        actual shouldBeEqual expect

        val actual1 = buildTree(intArrayOf(3,9,8,10,20,15,7), intArrayOf(8,9,10,3,15,20,7))!!
        val expect1 = TreeNode.of(3,9,20,8,10,15,7)!!

        actual1 shouldBeEqual expect1
    }
}
