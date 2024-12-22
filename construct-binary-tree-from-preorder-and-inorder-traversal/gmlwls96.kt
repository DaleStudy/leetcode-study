class Solution {
    // 시간 : O(n^2)
    fun buildTree(preorder: IntArray, inorder: IntArray): TreeNode? {
        if (preorder.isEmpty() || inorder.isEmpty()) {
            return null
        }
        val value = preorder[0]
        var mid = inorder.indexOf(value)
        if (mid < 0) {
            mid = 0
        }
        val leftNode = buildTree(
            preorder.slice(1..preorder.lastIndex).toIntArray(),
            inorder.slice(0 until mid).toIntArray())
        val rightNode = buildTree(
            preorder.slice(2..preorder.lastIndex).toIntArray(),
            inorder.slice(mid + 1..inorder.lastIndex).toIntArray()
        )

        return TreeNode(value).apply {
            left = leftNode
            right = rightNode
        }
    }
}
