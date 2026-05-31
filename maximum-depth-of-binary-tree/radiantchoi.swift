/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func maxDepth(_ root: TreeNode?) -> Int {
        var result = 0

        traverse(root, 0, &result)

        return result
    }

    func traverse(_ node: TreeNode?, _ current: Int, _ result: inout Int) {
        guard let node else {
            result = max(current, result)
            return
        }

        let newCurrent = current + 1

        traverse(node.left, newCurrent, &result)
        traverse(node.right, newCurrent, &result)
    }
}
