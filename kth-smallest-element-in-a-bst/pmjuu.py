'''
시간 복잡도: O(n)
공간 복잡도: O(n)
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                values.append(node.val)
                inorder_traversal(node.right)
        
        values = []
        inorder_traversal(root)

        return values[k - 1]
