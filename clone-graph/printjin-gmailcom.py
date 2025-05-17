from typing import Optional
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        old_to_new = {}
        def dfs(n):
            if n in old_to_new:
                return old_to_new[n]
            copy = Node(n.val)
            old_to_new[n] = copy
            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
