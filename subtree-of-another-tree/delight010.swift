class Solution {
    // Time O(M * N)
    // Space O(M + N)
    func isSubtree(_ root: TreeNode?, _ subRoot: TreeNode?) -> Bool {
        if let root = root, let subRoot = subRoot {
            return dfs(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
        }
        
        return root == nil && subRoot == nil
    }
    
    private func dfs(_ root: TreeNode?, subRoot: TreeNode?) -> Bool {
        if let root = root, let subRoot = subRoot {
            return root.val == subRoot.val && dfs(root.left, subRoot.left) && dfs(root.right, subRoot.right)
        }
        
        return root == nil && subRoot == nil
    }
}
 
