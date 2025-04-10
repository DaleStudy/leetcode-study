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

//<문제>
///이진 트리의 루트가 주어졌을 때, 이것이 유효한 이진 검색 트리(BST)인지 판단하세요.
///유효한 BST는 다음과 같이 정의됩니다:
///- 노드의 왼쪽 하위 트리에는 노드의 키보다 작은 키를 가진 노드만 포함되고,
///- 노드의 오른쪽 하위 트리에는 노드의 키보다 큰 키를 가진 노드만 포함됩니다.
///- 또한 왼쪽과 오른쪽 하위 트리는 모두 이진 검색 트리여야 합니다.

class Solution {
    func isValidBST(_ root: TreeNode?) -> Bool {
        return checkingBST(root, min: nil, max: nil)
    }

    // min과 max는 현재 노드가 가질 수 있는 값의 범위
    func checkingBST(_ node: TreeNode?, min: Int?, max: Int?) -> Bool {
        guard let node else { return true } // nil이면 유효한 트리
        
        if let min = min, node.val <= min {
            return false
        }
        if let max = max, node.val >= max {
            return false
        }

        // 왼쪽은 max = node.val, 오른쪽은 min = node.val
        return checkingBST(node.left, min: min, max: node.val)
            && checkingBST(node.right, min: node.val, max: max)
    }
}

