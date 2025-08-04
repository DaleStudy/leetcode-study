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
        """
        Time Complexity: O(n + m) (n은 노드의 개수, m은 간선 개수)
        Space Complexity: O(n) (노드 개수만큼 맵 사용)
        """
        # clones_map 딕셔너리
        # key: 원본 노드 객체
        # value: 복제 노드 객체
        clones_map = {} # 노드를 복제 하고 바로 등록할 딕셔너리

        def dfs_clone(original_node: Optional['Node']) -> Optional['Node']:
            # 원본 노드가 비어있으면 None 반환
            if not original_node:
                return None

            # 원본 노드가 clones_map에 있다면
            # 전에 복제 했음을 의미, 해당 복제 노드 객체를 반환
            if original_node in clones_map:
                return clones_map[original_node]

            # 새로운 복제 노드 생성 후 val 복사
            new_clone = Node(original_node.val)
            # 위에서 생성된 복제 노드를 clones_map에 등록 
            clones_map[original_node] = new_clone

            # 원본 노드의 이웃을 복사
            if original_node.neighbors:
                # 각각의 이웃 노드들에 대해 처리
                for original_neighbor in original_node.neighbors:
                    # 재귀적으로 dfs_clone 호출하여 clone
                    # (위 작업에 의해 이미 복제 했다면, 복제된 객체가 반환 될 것)
                    cloned_neighbor = dfs_clone(original_neighbor)
                    # 새로 복제된 노드 new_clone의 이웃으로 추가
                    new_clone.neighbors.append(cloned_neighbor)

            return new_clone # 완성된 복제 노드 반환
            
        # 시작 노드로부터 재귀적인 복제 시작
        return dfs_clone(node)
