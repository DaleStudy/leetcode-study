from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        copied = {}

        def traverse(node: Optional["Node"]) -> Optional["Node"]:
            if node in copied:
                return copied[node]

            newNode = Node(node.val)
            copied[node] = newNode
            newNode.neighbors = [traverse(neighbor) for neighbor in node.neighbors]

            return newNode

        return traverse(node)


# Time Complexity: O(n), where n is the number of nodes in the graph, reflecting that each node is visited exactly once.
# Space Complexity: O(n), where n is the number of nodes in the graph.
#   This accounts for the space needed to store a copy of each node
#   and the maximum potential size of the recursion call stack, which corresponds to the number of nodes.
