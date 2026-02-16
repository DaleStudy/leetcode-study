// Definition for a binary tree node.
public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
}

class Solution {
    func lowestCommonAncestor(_ root: TreeNode?, _ p: TreeNode?, _ q: TreeNode?) -> TreeNode? {
        guard let p, let q else { return nil }

        var common = root

        // BST에서 같은 조상을 가진다는 건, 해당 조상의 "범주" 안에 있단 뜻
        // 왼쪽은 해당 값보다 작은 값, 오른쪽은 해당 값보다 큰 값이 있음을 보장
        while let ancestor = common, ancestor.val != p.val, ancestor.val != q.val {
            if p.val < ancestor.val && q.val < ancestor.val {
                common = common?.left
            } else if p.val > ancestor.val && q.val > ancestor.val {
                common = common?.right
            } else {
                break
            }
        }

        return common
    }
}
