"""
Solution: 
    BST 의 특징을 이용해 풀이할 예정이다.
    1) cur.val 보다 p.val, q.val 이 작으면 왼쪽 트리에 LCA 가 있다.
    2) cur.val 보다 p.val, q.val 이 크면 오른쪽 트리에 LCA 가 있다.
    3) 나머지 케이스는 본인이 LCA 이다.

Time: O(log(n))
Space: O(1)

"""


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur


"""
Solution: 재귀
Time: O(log(n))
Space: O(log(n))
"""


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
