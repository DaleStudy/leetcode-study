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
    guard let root else { return nil }
    if root.val < p!.val, root.val < q!.val {
      return lowestCommonAncestor(root.right, p, q)
    } else if root.val > p!.val, root.val > q!.val {
      return lowestCommonAncestor(root.left, p, q)
    }
    return root
  }
}
