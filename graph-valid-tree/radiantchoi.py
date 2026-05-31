from typing import List

# 어떤 그래프가 Valid Tree려면?
# 순환이 발생하지 않으면서, 모든 노드가 연결되어 있어야 한다.
# n개의 노드를 모두 연결하는 데 필요한 간선의 갯수는 n - 1개
# 순환 발생 탐지 -> Union Find

class Solution:
    def find(self, parent: List[int], n: int) -> int:
        if parent[n] == n:
            return n
        
        parent[n] = self.find(parent, parent[n])
        return parent[n]
    
    def union(self, parent: List[int], left: int, right: int) -> bool:
        left_parent = self.find(parent, left)
        right_parent = self.find(parent, right)
        
        if left_parent == right_parent:
            return False
        
        parent[right_parent] = left_parent
        return True
    
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        parents = list(range(n))
        
        for edge in edges:
            # Union Find에서 False가 반환된다는 것은 순환이 발생한다는 것
            if not self.union(parents, edge[0], edge[1]):
                return False
        
        return len(edges) == n - 1
