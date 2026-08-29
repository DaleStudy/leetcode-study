from collections import deque

class Solution:
    # Time Complexity: O(n*m), n: len(heights), m: len(heights[0])
    # Space Complexity: O(n*m), n: len(heights), m: len(heights[0])
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = []
        pacific, atlantic = set(), set()

        # bfs
        def bfs(visited):
            q = deque(visited)

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and heights[r][c] <= heights[nr][nc]:
                        q.append((nr, nc))
                        visited.add((nr, nc))

        # insert cells on the border
        pacific = {(r, 0) for r in range(ROWS)} | {(0, c) for c in range(COLS)}
        atlantic = {(r, COLS-1) for r in range(ROWS)} | {(ROWS-1, c) for c in range(COLS)}

        bfs(pacific) # check pacific ocean -> atlantic ocean
        bfs(atlantic) # check atlantic ocean -> pacific ocean

        return [[r, c] for r in range(ROWS) for c in range(COLS) if (r, c) in pacific and (r, c) in atlantic]
