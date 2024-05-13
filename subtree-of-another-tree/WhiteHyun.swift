//  
//  572. Subtree of Another Tree
//  https://leetcode.com/problems/subtree-of-another-tree/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/05/12.
//  

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
extension TreeNode: Equatable {
  public static func == (lhs: TreeNode, rhs: TreeNode) -> Bool {
    lhs.val == rhs.val && lhs.left == rhs.left && lhs.right == rhs.right
  }
}

final class Solution {
  func isSubtree(_ node: TreeNode?, _ subRoot: TreeNode?) -> Bool {
    if node == subRoot { return true }
    else if node?.left != nil, isSubtree(node?.left, subRoot) { return true }
    else if node?.right != nil, isSubtree(node?.right, subRoot) { return true }
    return false
  }
}
