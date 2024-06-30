"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/

Solution:
    To clone a graph, we can use a depth-first search (DFS) to explore all nodes and their neighbors.
    We can create a helper function that takes a node and returns its clone.
    
    - We can use a dictionary to map old nodes to new nodes.
    - We can create a helper function to clone a node and its neighbors.
        - If the node has already been cloned, we return the clone.
        - Otherwise, we create a new clone and add it to the dictionary.
        - We clone all neighbors of the node recursively.
        - We return the clone.
    - We start the DFS from the given node and return the clone.

Time complexity: O(n+m)
    - n is the number of nodes in the graph.
    - m is the number of edges in the graph.
    - We explore all nodes and edges once.

Space complexity: O(n)
    - We use a dictionary to keep track of the mapping between old nodes and new nodes.
    - The maximum depth of the recursive call stack is the number of nodes in the graph.
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            clone = Node(node.val)
            old_to_new[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
