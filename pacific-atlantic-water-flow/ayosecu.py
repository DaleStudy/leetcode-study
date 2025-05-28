from typing import List
from collections import deque

class Solution:
    """
        - Time Complexity: O(mn)
        - Space Complexity: O(mn)
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        # Visit checking for each ocean
        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]

        def bfs(q, visited):
            dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            while q:
                r, c = q.popleft()
                for dx, dy in dir:
                    next_r, next_c = r + dx, c + dy
                    # checking next cell is not visited and higher than current cell
                    if ( 0 <= next_r < m and 0 <= next_c < n and not visited[next_r][next_c]
                        and heights[next_r][next_c] >= heights[r][c] ):
                        visited[next_r][next_c] = True
                        q.append((next_r, next_c))
                    
        p_dq, a_dq = deque(), deque()

        for i in range(m):
            # left side (pacific)
            p_dq.append((i, 0))
            p_visited[i][0] = True
            # right side (atlantic)
            a_dq.append((i, n - 1))
            a_visited[i][n - 1] = True
        
        for j in range(n):
            # top side (pacific)
            p_dq.append((0, j))
            p_visited[0][j] = True
            # bottom side (atlantic)
            a_dq.append((m - 1, j))
            a_visited[m - 1][j] = True
        
        bfs(p_dq, p_visited)
        bfs(a_dq, a_visited)

        result = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    # both of oceans are accessible
                    result.append([i, j])
        
        return result

tc = [
        ([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),
        ([[1]], [[0,0]])
]

sol = Solution()
for i, (h, e) in enumerate(tc, 1):
    r = sol.pacificAtlantic(h)
    print(f"TC {i} is Passed!" if r == e else f"TC {i} is Failed! - Expected: {e}, Result: {r}")
