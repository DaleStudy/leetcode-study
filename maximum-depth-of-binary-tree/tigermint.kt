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
    fun maxDepth(root: TreeNode?): Int {
        if (root == null) return 0

        var maxDepth = 0

        fun dfs(node: TreeNode, depth: Int) {
            //leaf node
            if (node.left == null && node.right == null) maxDepth = maxOf(maxDepth, depth)

            if (node.left != null) dfs(node.left!!, depth + 1)
            if (node.right != null) dfs(node.right!!, depth + 1)
        }

        dfs(root!!, 1)

        return maxDepth
    }

}
