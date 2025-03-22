'''
시간 복잡도: O(V + E)
- 그래프의 모든 노드를 한 번씩 방문해야 하므로 O(V)
- 각 노드의 모든 간선을 한 번씩 탐색해야 하므로 O(E)
- 따라서 전체 시간 복잡도는 O(V + E)

공간 복잡도: O(V + E)
- 클론 노드를 저장하는 딕셔너리(clones): O(V)
- BFS 탐색을 위한 큐(queue): O(V)
- 복제된 그래프의 노드와 간선 저장 공간: O(V + E)
'''

from typing import Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = { node.val: Node(node.val) }
        queue = deque([node])

        while queue:
            current_node = queue.popleft()

            for neighbor in current_node.neighbors:
                # add neighbors
                if neighbor.val not in clones.keys():
                    queue.append(neighbor)
                    clones[neighbor.val] = Node(neighbor.val)
                    
                clones[current_node.val].neighbors.append(clones[neighbor.val])
        
        return clones[node.val]
