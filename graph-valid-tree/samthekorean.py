# O(n+e) where n is number of nodes and e is the number of edges.
# O(n+e) where n is number of nodes and e is the number of edges.
class Solution:
    def validTree(self, numNodes: int, connections: List[List[int]]) -> bool:
        adjacencyList = [[] for _ in range(numNodes)]
        for src, dst in connections:
            adjacencyList[src].append(dst)
            adjacencyList[dst].append(src)

        visitedNodes = set()

        def detectCycle(currentNode, previousNode):
            if currentNode in visitedNodes:
                return True
            visitedNodes.add(currentNode)
            for neighbor in adjacencyList[currentNode]:
                if neighbor == previousNode:
                    continue
                if detectCycle(neighbor, currentNode):
                    return True
            return False

        if detectCycle(0, -1):
            return False
        return len(visitedNodes) == numNodes
