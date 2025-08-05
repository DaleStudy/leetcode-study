/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun isValidBST(root: TreeNode?): Boolean {
        val values = mutableListOf<Int>()
        inorderTraversal(root, values)

        for (i in 1 until values.size) {
            if (values[i] <= values[i - 1]) return false
        }

        return true
    }

    private fun inorderTraversal(root: TreeNode?, values: MutableList<Int>) {
        if (root == null) return

        inorderTraversal(root.left, values)
        values.add(root.`val`)
        inorderTraversal(root.right, values)
    }
}
