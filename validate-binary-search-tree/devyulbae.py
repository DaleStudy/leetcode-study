"""
Blind 75 - LeetCode Problem 98: Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
이진 탐색 트리인지 확인하기

"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        