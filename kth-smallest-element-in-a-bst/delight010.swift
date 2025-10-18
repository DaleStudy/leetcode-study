class Solution {
    // Time O(k)
    // Space O(height of Tree)
    func kthSmallest(_ root: TreeNode?, _ k: Int) -> Int {
        var count = 0
        var result = root!.val
        
        inorderTree(root, &count, k, &result)
        
        return result
    }
    
    private func inorderTree(_ node: TreeNode?, _ count: inout Int, _ k: Int, _ result: inout Int) {
        guard let node = node else { return }
        if count == k { return }
        
        // left search
        inorderTree(node.left, &count, k, &result)
        
        // current node
        count += 1
        if count == k {
            result = node.val
            return
        }
        
        // right search
        inorderTree(node.right, &count, k, &result)
    }
}
 
