// Definition for a binary tree node.
public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    // 종료조건을 설정하고 재귀로 돌려서 트리 전체를 점검 - DFS
    func isSameTree(_ p: TreeNode?, _ q: TreeNode?) -> Bool {
        // 둘 다 nil이면 같은 것으로 취급 - TreeNode는 Equatable을 채택하지 않아서, p == q와 같은 직접 비교는 불가능
        if p == nil && q == nil { return true }
        // 둘 다 nil인 경우가 아니라면, 한 쪽이라도 nil이면 같은 것이 아니므로 false
        guard let p, let q else { return false }
        // 값이 같지 않으면 false
        guard p.val == q.val else { return false }

        // 둘 다 nil이 아니고, 값이 같음까지 검증한 상태
        if p.isLeafNode && q.isLeafNode {
            // 자식이 없다면 true 반환
            return true
        } else {
            // 자식이 있다면 자식들에 대해 각각 검사 수행
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
        }
    }
}

extension TreeNode {
    var isLeafNode: Bool {
        left == nil && right == nil
    }
}
