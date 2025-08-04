class Solution {
    // TC : O(H+K)
    // SC: O(H)
    private var K: Int = 0
    fun kthSmallest(root: TreeNode?, k: Int): Int {
        K = k
        return traverse(root)!!.`val`
    }

    fun traverse(cur: TreeNode?): TreeNode?{
        if(cur == null) return cur

        val result = traverse(cur.left)
        K--
        if(K == 0) return cur
        return result ?: traverse(cur.right)
    }
}
