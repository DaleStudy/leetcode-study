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
        
        // 굳이 Nullable을 담을 필요 없으므로 Queue<TreeNode> 사용
        val queue: Queue<TreeNode> = LinkedList()
        queue.add(root)
        
        var maxDepth = 0

        while (queue.isNotEmpty()) {
            val levelSize = queue.size // 현재 레벨에 있는 노드의 개수
            maxDepth++ // 레벨 진입 시 깊이 1 증가

            // 현재 레벨에 있는 노드들을 몽땅 꺼내고, 다음 레벨(자식들)을 넣음
            repeat(levelSize) {
                val curNode = queue.poll() // LinkedList에서는 remove()보다 poll()이 안전
                
                // 자식 노드가 있으면 큐에 추가 (다음 레벨 예비군)
                curNode.left?.let { queue.add(it) }
                curNode.right?.let { queue.add(it) }
            }
        }

        return maxDepth
    }
}
