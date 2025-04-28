//
//  Merge_Two_Sorted_Lists.swift
//  Algorithm
//
//  Created by 안세훈 on 4/22/25.
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
    func maxDepth(_ root: TreeNode?) -> Int {
       guard root != nil else { return 0 } //nil일 경우 깊이 0으로 처리
       
       var leftdepth = maxDepth(root?.left) //왼쪽 노드의 깊이 탐색
       var rightdepth = maxDepth(root?.right) //오른쪽 노드의 깊이 탐색
       
       return max(leftdepth, rightdepth) + 1 //더 깊은 곳과 자기 자신을 위해 + 1을 해서 리턴.
    }
}
