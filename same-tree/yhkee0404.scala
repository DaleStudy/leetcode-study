/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def isSameTree(p: TreeNode, q: TreeNode): Boolean = {
        return p == null && q == null
                || (
                    p != null
                    && q != null
                    && p.value == q.value
                    && this.isSameTree(p.left, q.left)
                    && this.isSameTree(p.right, q.right)
                )
    }
}
