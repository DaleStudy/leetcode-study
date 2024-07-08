"""
323. Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Solution:
    To solve this problem, we can use the depth-first search (DFS) algorithm.
    We can create an adjacency list to represent the graph.
    Then, we can perform a DFS starting from each node to count the number of connected components.
    We keep track of visited nodes to avoid revisiting nodes.
    The number of connected components is the number of times we perform DFS.

Time complexity: O(n+m)
    - We visit each node and edge once.
    - The DFS has a time complexity of O(n+m).

Space complexity: O(n+m)
    - We use an adjacency list to store the graph.
    - The space complexity is O(n+m) for the adjacency list and visited set.

"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize the graph as an adjacency list
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Set to keep track of visited nodes
        visited = set()

        # Function to perform DFS
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        # Count connected components
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i)

        return count
