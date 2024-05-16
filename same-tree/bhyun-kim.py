"""
100. Same Tree
https://leetcode.com/problems/same-tree/description/

Solution:
    This is a recursive problem that requires comparing two binary trees.
    We can use a recursive function to compare the values of the nodes in the two binary trees.
    If the values of the nodes are equal, we can compare the left and right subtrees recursively.
    The base case is when both nodes are None, in which case we return True.
    
    1. Check if the values of the nodes are equal.
    2. Compare the left and right subtrees recursively.
    3. Return True if the values of the nodes are equal and the left and right subtrees are equal, otherwise return False.
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q == None:
            return True

        if hasattr(p, "val") and hasattr(q, "val"):
            if p.val != q.val:
                return False

            left_same = self.isSameTree(p.left, q.left)
            right_same = self.isSameTree(p.right, q.right)

            return left_same == right_same == True

        else:
            return False
