"""
시간 복잡도: O(V + E) V: 노드 개수, E: 간선 개수
공간 복잡도: O(V)
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        clone = Node(node.val)
        vis = {node: clone}
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for nxt in cur.neighbors:
                if nxt not in vis:
                    vis[nxt] = Node(nxt.val)
                    queue.append(nxt)
                vis[cur].neighbors.append(vis[nxt])
        return clone
