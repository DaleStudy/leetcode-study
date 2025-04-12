//
//  251.swift
//  Algorithm
//
//  Created by 안세훈 on 4/8/25.
//

//Validate Binary Search Tree

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
    func isValidBST(_ root: TreeNode?) -> Bool {
        return validate(root, min: nil, max: nil)
    }

    private func validate(_ node: TreeNode?, min: Int?, max: Int?) -> Bool {
        guard let node = node else { return true }

        if let min = min, node.val <= min { return false }
        if let max = max, node.val >= max { return false }

        return validate(node.left, min: min, max: node.val) &&
               validate(node.right, min: node.val, max: max)
    }
}
