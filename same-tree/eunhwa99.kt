package leetcode_study

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

// Time Complexity: O(n)
// Space Complexity: O(h) where h is the height of the tree (재귀함수로 인한 공간 복잡도)
class Solution {
    fun isSameTree(p: TreeNode?, q: TreeNode?): Boolean {
        return if (p == null && q == null) {
            true
        } else if (p == null || q == null || p.`val` != q.`val`) {
            false
        } else {
            isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
        }
    }
}
