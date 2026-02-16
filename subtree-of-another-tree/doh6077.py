from collections import deque
from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/description/
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Use BFS => Queue 
        # Edge cases
        if subRoot is None:
            return True
        if root is None:
            return False

        def helper(node: Optional[TreeNode], subNode: Optional[TreeNode]) -> bool:
            if node is None and subNode is None:
                return True
            if node is None or subNode is None:
                return False
            if node.val != subNode.val:
                return False
            return helper(node.left, subNode.left) and helper(node.right, subNode.right)

        q = deque([root])

        while q:
            curr = q.popleft()

            # Only attempt full compare when root values match
            if curr.val == subRoot.val and helper(curr, subRoot):
                return True

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        return False
