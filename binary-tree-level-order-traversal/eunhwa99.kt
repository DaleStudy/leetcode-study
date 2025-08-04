// https://leetcode.com/problems/binary-tree-level-order-traversal/description/
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
    fun levelOrder(root: TreeNode?): List<List<Int>> {
        val result = mutableListOf<List<Int>>()
        if(root == null) return result

        val queue: ArrayDeque<TreeNode> = ArrayDeque()
        queue.add(root)
        
        while (queue.isNotEmpty()) {
            val levelSize = queue.size
            val level = mutableListOf<Int>()
            repeat(levelSize) {
                val node = queue.removeFirst()
                level.add(node.`val`)
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            result.add(level)
        }
        return result
    }
}
