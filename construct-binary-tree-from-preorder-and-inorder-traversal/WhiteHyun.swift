//  
//  105. Construct Binary Tree from Preorder and Inorder Traversal
//  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
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
  func buildTree(_ preorder: [Int], _ inorder: [Int]) -> TreeNode? {
    let indices: [Int: Int] = Dictionary(uniqueKeysWithValues: inorder.enumerated().map { ($0.element, $0.offset) })

    var preorderIndex = 0

    func build(_ left: Int, _ right: Int) -> TreeNode? {
      if left > right { return nil }

      let rootValue = preorder[preorderIndex]
      preorderIndex += 1
      let root = TreeNode(rootValue)

      let mid = indices[rootValue]!

      root.left = build(left, mid - 1)
      root.right = build(mid + 1, right)

      return root
    }

    return build(0, inorder.count - 1)
  }
}
