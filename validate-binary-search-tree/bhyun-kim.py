"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/


"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Solution1:
    Recursion
    In the given problem, the subtree of a node has a range of values according to the previous nodes. 
    Thus, we can define a function that checks the validity of the subtree of a node with the range of values.

    - Define a function that checks the validity of the subtree of a node with the range of values
    - Check the validity of the left subtree and the right subtree
        - with the range of values that the left subtree and the right subtree should have
        - If left < root < right, the subtree is valid
    - If the left subtree and the right subtree are valid, call the function recursively for the left and right subtrees.
        - before calling the function, update the range of values for the left and right subtrees
    - If the left subtree and the right subtree are valid, return True

Time complexity: O(N)
    - The function is called recursively for each node

Space complexity: O(N)
    - The function stores the range of values for each node
"""


class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maximum = float("inf")
        minimum = float("-inf")
        return self.isValidSubTree(root, maximum, minimum)

    def isValidSubTree(self, root, maximum, minimum):

        if root is None:
            return True

        if not minimum < root.val < maximum: 
            return False 
        
        return self.isValidSubTree(
            root.left, root.val, minimum
            ) and self.isValidSubTree(
            root.right, maximum, root.val 
            )
