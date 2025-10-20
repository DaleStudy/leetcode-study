public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    // Time O(n)
    // Space best O(log n)
    // Space worst O(n)
    func isSameTree(_ p: TreeNode?, _ q: TreeNode?) -> Bool {
        return dfs(p, q)
    }
    
    private func dfs(_ p: TreeNode?, _ q: TreeNode?) -> Bool {
        if p == nil && q == nil {
            return true
        }
        
        guard let p = p else { return false }
        guard let q = q else { return false }
        
        if p.val != q.val {
            return false
        }
        
        return dfs(p.left, q.left) && dfs(p.right, q.right)
    }
}
 
