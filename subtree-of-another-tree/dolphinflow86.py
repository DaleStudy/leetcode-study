# M and N are the number of nodes in root and subRoot trees respectively.
# TC: O(M * N) - in the worst case, is_same is checked for every node in root
# SC: O(H) - recursion stack memory bounded by the height of root tree (up to O(M))

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isSubtree(self, root: Optional["TreeNode"], subRoot: Optional["TreeNode"]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def is_same(s: Optional["TreeNode"], t: Optional["TreeNode"]) -> bool:
            if not s and not t:
                return True
            if not s or not t or s.val != t.val:
                return False
            return is_same(s.left, t.left) and is_same(s.right, t.right)

        if is_same(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
