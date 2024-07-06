"""
261. Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/

Solution:
    To solve this problem, we can use the depth-first search (DFS) algorithm.
    We can create an adjacency list to represent the graph.
    Then, we can perform a DFS starting from node 0 to check if all nodes are visited.
    If all nodes are visited, we return True; otherwise, we return False.

Time complexity: O(n)
    - We visit each node once.
    - The DFS has a time complexity of O(n).

Space complexity: O(n)
    - We use an adjacency list to store the graph.
    - The space complexity is O(n) for the adjacency list.
"""


from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # Initialize adjacency list
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Function to perform DFS
        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited or not dfs(neighbor, node):
                    return False
            return True

        visited = set()

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # Check if all nodes are visited
        return len(visited) == n
