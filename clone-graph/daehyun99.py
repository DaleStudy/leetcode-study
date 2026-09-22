# Time: O(N + E
# Space: O(N)
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        have_to_look = set()
        seen = set()
        copied = {}

        have_to_look.add(node)

        while len(have_to_look) > 0 :
            curr = have_to_look.pop()
            if curr is not None:
                if curr.val not in copied:
                    copied[curr.val] = Node(curr.val, None)
                for neighbor in curr.neighbors:
                    if neighbor.val not in copied:
                        copied[neighbor.val] = Node(neighbor.val, None)
                        if neighbor.val not in seen:
                            have_to_look.add(neighbor)
                    copied[curr.val].neighbors.append(copied[neighbor.val])
                seen.add(curr.val)

        return copied.get(1, None)

