"""
[문제풀이]
# Inputs

# Outputs

# Constraints

# Ideas

[회고]

"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return

        clone = Node(node.val)
        clones = {node: clone}

        q = deque([node])  # 해당 라인 답지 참고

        while q:
            node = q.popleft()

            for nei in node.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)  # 답지 참고
                    q.append(nei)

                clones[node].neighbors.append(clones[nei])  # 답지 참고

        return clone


