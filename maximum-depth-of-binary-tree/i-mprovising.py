"""
Time complexity O(n)
"""
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        max_depth = 0

        # bfs
        q = deque([[root, 1]])
        while(q):
            node, depth = q.pop()
            if max_depth < depth:
                max_depth = depth
            if node.left:
                q.append([node.left, depth+1])
            if node.right:
                q.append([node.right, depth+1])

        return max_depth
