//  
//  98. Validate Binary Search Tree
//  https://leetcode.com/problems/validate-binary-search-tree/description/
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
  func isValidBST(_ node: TreeNode?) -> Bool {
    guard let node else { return true }

    var left = node.left
    var right = node.right

    while left?.right != nil {
      left = left?.right
    }
    while right?.left != nil {
      right = right?.left
    }

    if left?.val ?? .min < node.val,
       node.val < right?.val ?? .max {
      return isValidBST(node.left) && isValidBST(node.right)
    }

    return false
  }
}
