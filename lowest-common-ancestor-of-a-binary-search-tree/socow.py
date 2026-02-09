"""
235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Solution:
    BST의 특성을 활용한다.
    1) p, q 모두 현재 노드보다 작으면 → LCA는 왼쪽 서브트리에 존재
    2) p, q 모두 현재 노드보다 크면 → LCA는 오른쪽 서브트리에 존재
    3) 그 외의 경우 → 현재 노드가 LCA (p, q가 갈라지는 지점)

Time: O(log n) - 균형 BST 기준, 최악의 경우 O(n)
Space: O(1)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
