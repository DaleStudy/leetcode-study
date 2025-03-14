'''
시간 복잡도: O(n)
공간 복잡도: O(n)
'''

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root]) if root else []
        result = []

        while queue:
            same_level_nodes = []

            for _ in range(len(queue)):
                node = queue.popleft()
                same_level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(same_level_nodes)

        return result

            