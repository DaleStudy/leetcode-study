"""
Blind 75 - LeetCode Problem 98: Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

중위 순회 - 왼쪽 서브트리 -> 루트 -> 오른쪽 서브트리
중위 순회한 값이 오름차순인지 확인하면 된다.
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:    # root = [2,1,3] answer = True 
    def traverse(self, node: Optional[TreeNode], inorder: List[int]) -> None:
        if not node:
            return
        self.traverse(node.left, inorder)
        inorder.append(node.val)
        self.traverse(node.right, inorder)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []
        self.traverse(root, inorder)

        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False
            
        return True

