/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def kthSmallest(root: TreeNode, k: Int): Int = {
        count(root, k, -1)
    }
    def count(root: TreeNode, k: Int, n: Int): Int = {
        if (root == null) {
            return n
        }
        val u = count(root.left, k, n)
        if (u >= 0) {
            return u
        }
        if (- u == k) {
            return root.value
        }
        count(root.right, k, u - 1)
    }
}
