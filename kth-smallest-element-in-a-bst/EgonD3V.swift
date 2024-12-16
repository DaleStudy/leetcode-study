import Foundation

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
    
    /*
        Runtime: 28 ms (Beats 46.95%)
        Analyze Complexity: O(n)
        Memory: 16.52 MB (Beats 53.05%)
    */
    func kthSmallest(_ root: TreeNode?, _ k: Int) -> Int {
        func inorderTraverse(_ root: TreeNode?, _ k: Int) {
            guard let root = root, visited.count < k else {
                return
            }
            
            inorderTraverse(root.left, k)
            if visited.count < k {
                visited.append(root.val)
            }
            inorderTraverse(root.right, k)
        }
        
        var visited: [Int] = []
        inorderTraverse(root, k)

        return visited[k - 1]
    }
}
