"""
📚 417. Pacific Atlantic Water Flow

📌 문제 요약
- m x n 섬이 있고, 각 칸에 높이가 있음
- 왼쪽/위 = 태평양(Pacific), 오른쪽/아래 = 대서양(Atlantic)
- 물은 높은 곳 → 낮거나 같은 곳으로만 흐름
- 두 바다 모두에 물이 도달할 수 있는 좌표 찾기!

📝 문제 예시
heights = [
    [1, 2, 2, 3, 5],    ← 태평양 (위)
    [3, 2, 3, 4, 4],    
    [2, 4, 5, 3, 1],    
    [6, 7, 1, 4, 5],    
    [5, 1, 1, 2, 4]     → 대서양 (아래)
]
↑ 태평양 (왼쪽)        ↓ 대서양 (오른쪽)

결과: [[0,4], [1,3], [1,4], [2,2], [3,0], [3,1], [4,0]]

🎯 핵심 알고리즘
- 패턴: BFS/DFS (역방향 탐색)
- 시간복잡도: O(m × n)
- 공간복잡도: O(m × n)

💡 핵심 아이디어
1. 정방향(높→낮)으로 탐색하면 모든 점에서 시작해야 함 (비효율)
2. 역방향(바다→섬)으로! 바다에서 시작해서 올라갈 수 있는 곳 탐색
3. 태평양에서 갈 수 있는 곳 + 대서양에서 갈 수 있는 곳 = 정답!
"""

from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # 각 바다에서 도달 가능한 좌표 저장
        pacific = set()
        atlantic = set()
        
        def bfs(starts, reachable):
            queue = deque(starts)
            reachable.update(starts)
            
            while queue:
                r, c = queue.popleft()
                
                # 상하좌우 탐색
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    
                    # 범위 내 & 아직 안 감 & 올라갈 수 있음 (역방향!)
                    if (0 <= nr < m and 0 <= nc < n 
                        and (nr, nc) not in reachable
                        and heights[nr][nc] >= heights[r][c]):
                        queue.append((nr, nc))
                        reachable.add((nr, nc))
        
        # 태평양: 왼쪽 + 위쪽 가장자리에서 시작
        pacific_starts = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        bfs(pacific_starts, pacific)
        
        # 대서양: 오른쪽 + 아래쪽 가장자리에서 시작
        atlantic_starts = [(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n)]
        bfs(atlantic_starts, atlantic)
        
        # 교집합 = 두 바다 모두 도달 가능!
        return list(pacific & atlantic)

