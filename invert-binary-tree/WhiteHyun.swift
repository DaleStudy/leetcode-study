//
//  226. Invert Binary Tree.swift
//  https://leetcode.com/problems/invert-binary-tree/description/
//  Algorithm
//
//  Created by 홍승현 on 2024/05/04.
//

import Foundation

final class LeetCode226 {
  func invertTree(_ node: TreeNode?) -> TreeNode? {
    guard let node else { return nil }

    let left = node.left
    let right = node.right

    node.left = invertTree(right)
    node.right = invertTree(left)

    return node
  }
}
