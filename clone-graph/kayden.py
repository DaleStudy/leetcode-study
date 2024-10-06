from typing import Optional
from collections import deque


class Solution:
    # 시간복잡도: O(N) node 개수: N
    # 공간복잡도: O(N)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node:
            visited = {}
            copy = Node(val=node.val)
            visited[copy.val] = copy
            q = deque()
            q.append((copy, node))

            while q:
                cur, node = q.popleft()

                for idx, next_node in enumerate(node.neighbors):
                    if next_node.val not in visited:
                        new = Node(val=next_node.val)
                        visited[new.val] = new
                        q.append((new, next_node))
                    cur.neighbors.append(visited[next_node.val])

            return copy

        return node
