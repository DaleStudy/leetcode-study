class Solution {
    // Time O(height)
    // Space O(height)
    func lowestCommonAncestor(_ root: TreeNode?, _ p: TreeNode?, _ q: TreeNode?) -> TreeNode? {
        var current = root
        
        while current != nil {
            if let p = p, let q = q {
                if p.val < current!.val && q.val < current!.val {
                    current = current?.left
                } else if p.val > current!.val && q.val > current!.val {
                    current = current?.right
                } else {
                    return current
                }
            }
        }
        
        return current
    }
}
 
