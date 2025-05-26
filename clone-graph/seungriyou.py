# https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph_dfs(self, node: Optional['Node']) -> Optional['Node']:
        """
        [Complexity]
            - TC: O(n + m) (n = node 개수, m = edge 개수)
            - SC: O(n) (call stack & cache)

        [Approach]
            {val: node} 형태의 dict를 캐시처럼 활용하여, DFS로 접근한다.
            각 node를 복제해야 하므로, 원본 node의 복제본을 O(1)에 lookup 하려면 dict에 key를 Node.val 값으로 설정해야 한다.
        """
        copies = dict()  # {val: node}

        if not node:
            return None

        def copy_node(curr):
            # base condition: 이미 copies에 존재하는 node라면 반환
            if curr.val in copies:
                return copies[curr.val]

            # 현재 노드 복사
            copied_node = Node(val=curr.val)

            # copies에 추가
            copies[curr.val] = copied_node

            # neighbors를 순회하며, neighbors에 copy를 만들어 추가
            for ngbr in curr.neighbors:
                copied_node.neighbors.append(copy_node(ngbr))

            # 복사한 노드 반환
            return copied_node

        return copy_node(node)

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        [Complexity]
            - TC: O(n + m)
            - SC: O(n) (queue & cache)

        [Approach]
            {val: node} 형태의 dict를 캐시처럼 활용하여, BFS로 접근한다.
        """
        from collections import deque

        copies = dict()  # {val: node}

        if not node:
            return None

        q = deque([node])
        copied_root_node = Node(val=node.val)
        copies[node.val] = copied_root_node

        while q:
            curr = q.popleft()

            for ngbr in curr.neighbors:
                # ngbr.val이 캐시에 존재하지 않으면, copy 후 캐시에 저장
                if ngbr.val not in copies:
                    # ngbr의 복사본 생성 및 캐시에 저장
                    copies[ngbr.val] = Node(val=ngbr.val)

                    # ngbr은 아직 방문되지 않았으므로, q에 추가
                    q.append(ngbr)

                # curr 복사본의 neighbors에 ngbr 복사본 추가
                copies[curr.val].neighbors.append(copies[ngbr.val])

        return copied_root_node
