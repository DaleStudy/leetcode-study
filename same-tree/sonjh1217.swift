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
    // O(n) time, O(h) space h = 트리의 높이. 최악: n, 평균: log n
    func isSameTree(_ p: TreeNode?, _ q: TreeNode?) -> Bool {
        switch (p, q) {
        case (nil, nil):
            return true
        case let (p?, q?):
            return p.val == q.val
            && isSameTree(p.left, q.left)
            && isSameTree(p.right, q.right)
        default:
            return false
        }
    }
}
