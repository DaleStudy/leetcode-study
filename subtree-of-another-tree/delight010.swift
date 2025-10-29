class Solution {
    // Time O(M * N)
    // Space O(N)
    func isSubtree(_ root: TreeNode?, _ subRoot: TreeNode?) -> Bool {
        if let root = root, let subRoot = subRoot {
            if root.val == subRoot.val {
                return dfs(root.left, subRoot: subRoot.left) && dfs(root.right, subRoot: subRoot.right) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
            }
            return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
        }
        
        return false
    }
    
    private func dfs(_ root: TreeNode?, subRoot: TreeNode?) -> Bool {
        if root == nil && subRoot == nil {
            return true
        }
        
        if let root = root, let subRoot = subRoot {
            if root.val == subRoot.val {
                return dfs(root.left, subRoot: subRoot.left) && dfs(root.right, subRoot: subRoot.right)
            }
        }
        
        return false
    }
}
 
