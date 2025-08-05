class Solution {
    private var prev: Int?
    
    func isValidBST(_ root: TreeNode?) -> Bool {
        inorder(root)
    }
    
    private func inorder(_ root: TreeNode?) -> Bool {
        guard let root = root else { return true }
        
        guard inorder(root.left) else { return false }
        
        if let prev = prev, root.val <= prev { return false }
        prev = root.val
        
        return inorder(root.right)
    }
}
 
