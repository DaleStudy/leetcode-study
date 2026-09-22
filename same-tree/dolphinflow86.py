# N is the minimum number of nodes between trees p and q, and H is tree height.
# TC: O(N) - visits each node at most once comparing values
# SC: O(H) - recursion call stack proportional to tree height (O(N) in worst case)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
