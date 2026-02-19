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
    func isSubtree(_ root: TreeNode?, _ subRoot: TreeNode?) -> Bool {
        // 원소가 0개인 트리는 모든 트리의 서브트리로 간주 - 문제 내에서는 불가능한 조건
        if subRoot == nil { return true }
        
        // 이외의 경우 root가 반드시 존재해야 함
        guard let root else { return false }

        // 두 트리가 같은 경우 true 반환 - 자기 자신은 자신의 서브트리
        if root == subRoot { return true }

        // 이외의 경우 왼쪽 자식, 오른쪽 자식에 대해 서브트리 검사 수행
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
    }
}

// Equatable 프로토콜을 준수하도록 정의함으로써, == 연산자를 사용할 수 있도록 변경
extension TreeNode: Equatable {
    public static func ==(lhs: TreeNode, rhs: TreeNode) -> Bool {
        // Swift 컴파일러 특성상, 동일한 인스턴스를 비교할 때 === 연산자를 사용하면 O(1) 시간 내에 탐색 가능
        // 물론 참조 타입에서만 사용 가능하며, TreeNode는 class여서 사용 가능하다
        if lhs === rhs { return true }
        
        // 동일한 노드의 조건은, 값이 같고 왼쪽 자식이 같으며 오른쪽 자식이 같은 것
        return lhs.val == rhs.val && lhs.left == rhs.left && lhs.right == rhs.right
    }
}