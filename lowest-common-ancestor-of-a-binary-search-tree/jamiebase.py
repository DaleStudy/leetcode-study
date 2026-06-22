"""
# Approach
BST 의 특징을 이용해서 값의 대소 비교로 공통 조상을 찾습니다.

# Complexity
- Time complexity: 트리의 높이 H일때, O(H)
- Space complexity: O(1)
"""


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
