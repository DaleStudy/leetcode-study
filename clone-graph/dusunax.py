'''
# 133. Clone Graph
This is the problem for copying nodes, which helps you understand the concept of referencing a node & copying the node (creating a new node from the existing one).

👉 Perform recursion DFS with the correct escape condition and handling of NoneType.
'''

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
        if node is None:
            return None
            
        visited = {}
        
        def DFS(currNode):
            if currNode.val in visited:
                return visited[currNode.val]

            copiedNode = Node(currNode.val)
            visited[currNode.val] = copiedNode

            for neighbor in currNode.neighbors:
                copiedNode.neighbors.append(DFS(neighbor))

            return copiedNode

        return DFS(node)
