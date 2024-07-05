# O(n+e) where n is number of nodes and e is the number of edges.
# O(n+e) where n is number of nodes and e is the number of edges.
class Solution:
    def countComponents(self, numNodes: int, connections: List[List[int]]) -> int:
        adjacencyList = [[] for _ in range(numNodes)]
        for src, dst in connections:
            adjacencyList[src].append(dst)
            adjacencyList[dst].append(src)

        visitedNodes = set()

        def depthFirstSearch(node):
            visitedNodes.add(node)
            for neighbor in adjacencyList[node]:
                if neighbor not in visitedNodes:
                    depthFirstSearch(neighbor)

        componentCount = 0
        for node in range(numNodes):
            if node not in visitedNodes:
                componentCount += 1
                depthFirstSearch(node)
        return componentCount
