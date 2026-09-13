"""
시간 복잡도: O(N)
공간 복잡도: O(N)

BST에서 두 노드의 최소 공통 조상을 찾는 코드입니다.
두 노드의 값을 비교하여 최소 공통 조상을 찾는 방식으로 동작합니다.
"""
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root == p or root == q:
            return root

        p_compare = root.val > p.val
        q_compare = root.val > q.val

        if p_compare != q_compare:
            return root
        elif p_compare and q_compare:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
