"""
Solution: 
    1) 가장자리에서 시작해서 어디까지 올라갈수있는지 체크한다.
    2) 교집합을 찾는다.

Time: O(m * n)
Space: O(m * n)
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(visit, r, c):
            if (r, c) in visit:
                return
            visit.add((r, c))

            for i, j in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= i and i < ROWS and 0 <= j and j < COLS:
                    if heights[i][j] >= heights[r][c]:
                        dfs(visit, i, j)

        for i in range(ROWS):
            dfs(pacific, i, 0)
            dfs(atlantic, i, COLS - 1)
        for i in range(COLS):
            dfs(pacific, 0, i)
            dfs(atlantic, ROWS - 1, i)

        return list(pacific.intersection(atlantic))
