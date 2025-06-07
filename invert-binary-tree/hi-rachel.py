from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
재귀 풀이

TC: O(n), SC: O(n)
n = 트리 내의 노드 수
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
"""
스택 풀이

TC: O(n), SC: O(n)
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            stack += [node.left, node.right]
        return root
