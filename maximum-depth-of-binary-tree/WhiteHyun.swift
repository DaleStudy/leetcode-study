//  
//  104. Maximum Depth of Binary Tree
//  https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
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
final class Solution {
  func maxDepth(_ node: TreeNode?) -> Int {
    guard let node else { return 0 }

    return max(maxDepth(node.left), maxDepth(node.right)) + 1
  }
}
