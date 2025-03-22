'''
시간 복잡도: O(m * n)
- 각 바다에서 BFS를 한 번씩 수행하며, 각 셀을 최대 한 번씩 방문하므로 O(m * n)입니다.

공간 복잡도: O(m * n)
- BFS 탐색을 위한 큐와 방문한 셀을 저장하는 집합(set)이 필요하므로 O(m * n)입니다.
'''

from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(starts):
            queue = deque(starts)
            reachable = set(starts)
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and
                        (nr, nc) not in reachable and
                        heights[nr][nc] >= heights[r][c]):  # 물이 흐를 수 있는지 확인
                        queue.append((nr, nc))
                        reachable.add((nr, nc))
            
            return reachable

        # 태평양(왼쪽과 위쪽 가장자리)에서 시작하는 셀들
        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        # 대서양(오른쪽과 아래쪽 가장자리)에서 시작하는 셀들
        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]

        pacific_reach = bfs(pacific_starts)
        atlantic_reach = bfs(atlantic_starts)

        return list(pacific_reach & atlantic_reach)


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, reachable):
            reachable.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and
                    (nr, nc) not in reachable and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)

        pacific_reach, atlantic_reach = set(), set()

        for c in range(n):
            dfs(0, c, pacific_reach)
            dfs(m-1, c, atlantic_reach)

        for r in range(m):
            dfs(r, 0, pacific_reach)
            dfs(r, n-1, atlantic_reach)

        return list(pacific_reach & atlantic_reach)
