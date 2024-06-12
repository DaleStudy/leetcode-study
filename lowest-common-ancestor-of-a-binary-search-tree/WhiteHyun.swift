//  
//  235. Lowest Common Ancestor of a Binary Search Tree
//  https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/12.
//  

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */

class Solution {
  func lowestCommonAncestor(_ root: TreeNode?, _ p: TreeNode?, _ q: TreeNode?) -> TreeNode? {
    if root == nil { return nil }
    if root == p { return p }
    if root == q { return q }
    let left = lowestCommonAncestor(root?.left, p, q)
    let right = lowestCommonAncestor(root?.right, p, q)

    if left != nil, right != nil { return root }
    else if left != nil { return left }
    else { return right }
  }
}
