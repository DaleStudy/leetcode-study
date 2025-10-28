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
    // O(n * m) time / O(n) space
    func isSubtree(_ root: TreeNode?, _ subRoot: TreeNode?) -> Bool {
        let subRootNode = subRoot?.val

        var queue = [TreeNode]()
        guard let root = root else {
            return false
        }
        queue.append(root)
        var head = 0
        while queue.count > head {
            let currentNode = queue[head]
            head += 1
            if currentNode.val == subRootNode {
                if dfs(node: currentNode, subRoot: subRoot) {
                    return true
                }
            }
            
            if let left = currentNode.left {
                queue.append(left)
            }
            if let right = currentNode.right {
                queue.append(right)
            }
        }

        return false
    }

    func dfs(node: TreeNode?, subRoot: TreeNode?) -> Bool {
        guard let node = node, let subRoot = subRoot else {
            return node == nil && subRoot == nil
        }

        return node.val == subRoot.val
        && dfs(node: node.left, subRoot: subRoot.left)
        && dfs(node: node.right, subRoot: subRoot.right)
    }

}
