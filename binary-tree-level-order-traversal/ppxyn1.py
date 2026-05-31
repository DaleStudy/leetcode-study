# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# idea: BFS 
# Time Complexity: O(n)
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque([root])
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft() 
                if node:
                    level.append(node.val) 
                    if node.left:
                        q.append(node.left) 
                    if node.right:
                        q.append(node.right) 
            if level:
                ans.append(level)
        return ans


