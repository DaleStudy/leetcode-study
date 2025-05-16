"""
    풀이 :
        재귀를 이용해서 dfs풀이
        node를 복제하고 노드의 이웃된 노드에 대해서 재귀함수 호출을 통해 완성한다

        clones 딕셔너리에 이미 복사된 node들을 저장해서 이미 복제된 node에 대해
        함수를 호출하면 바로 return

    노드의 수 : V(정점 : Vertex) 이웃의 수 : E(간선 : Edge)라고 할 때

    TC : O(V + E)
        노드와 이웃에 대해서 순회하므로

    SC : O(V + E)
        해시테이블의 크기가 노드의 수에 비례해서 커지고 
        dfs의 호출스택은 이웃의 수만큼 쌓이므로
"""

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
        if not node :
            return None

        clones = {}
        
        def dfs(node : Optional['Node']) -> Optional['Node']:
            if node in clones :
                return clones[node]
            clone = Node(node.val)
            clones[node] = clone
            for nei in node.neighbors :
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node)
