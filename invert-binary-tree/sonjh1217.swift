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
    func invertTree(_ root: TreeNode?) -> TreeNode? {
        guard var invertedRoot = root else {
            return nil
        }

        func invert(node: TreeNode?) -> TreeNode? {
            guard var node = node else {
                return nil
            }

            if node.left == nil
            && node.right == nil {
                return node
            }

            let left = node.left
            node.left = invert(node: node.right)
            node.right = invert(node: left)
            return node
        }

        return invert(node: invertedRoot)
    }
}

