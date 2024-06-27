//  
//  230. Kth Smallest Element in a BST
//  https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
//  Dale-Study
//  
//  Created by WhiteHyun on 2024/06/27.
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
  private var triedCount: Int = 0
  func kthSmallest(_ node: TreeNode?, _ k: Int) -> Int {
    guard let node else { return -1 }
    let number = kthSmallest(node.left, k)
    if number != -1 { return number }
    if triedCount + 1 == k { return node.val }
    triedCount += 1
    return kthSmallest(node.right, k)
  }
}
