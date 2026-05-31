# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# idea : BFS
# Time Complexity : O(size of root * size of subRoot)
from collections import deque

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            node = queue.popleft()
            
            if node:
                if self.isSame(node, subRoot):
                    return True
                queue.append(node.left)
                queue.append(node.right)

        return False

    def isSame(self, r, s):
        if not r and not s:
            return True
        if not r or not s:
            return False
        if r.val != s.val:
            return False
        return self.isSame(r.left, s.left) and self.isSame(r.right, s.right)

