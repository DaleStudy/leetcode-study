class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid Tree
        # 1. no loop
        # 2. no disconnected node 
        # Use DFS and Hashset to track visited nodes 
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        def dfs(i, prev):
            # Base case
            if i in visit:
                return False
            visit.add(i)
            # check neighbor nodes 
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)
