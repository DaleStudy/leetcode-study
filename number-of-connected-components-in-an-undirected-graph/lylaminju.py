'''
n: 노드 개수 / e: 간선 개수
시간 복잡도: O(n + e)
공간 복잡도: O(n + e)
'''
from typing import List

class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(node):         
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        count = 0
        for node in graph:
            if node not in visited:
                count += 1
                dfs(node)
                
        return count

# Test function
def test():
    solution = Solution()
    test_cases = [
        (3, [[0, 1], [0, 2]], 1),
        (6, [[0, 1], [1, 2], [2, 3], [4, 5]], 2),
        (4, [[0, 1], [2, 3]], 2),
        (1, [], 1),
        (4, [[0, 1], [2, 3], [1, 2]], 1)
    ]
    
    for i, (n, edges, expected) in enumerate(test_cases):
        result = solution.count_components(n, edges)
        print(f"Test case {i+1}: Input: n={n}, edges={edges} -> Output: {result}, Expected: {expected}")
        if result != expected:
            print(f"# Test case {i+1} failed: expected {expected}, got {result}")
        print("\n")
    
# Run tests
test()
