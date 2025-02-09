'''
# 417. Pacific Atlantic Water Flow

## Time Complexity: O(n * m)
- dfs is called for each cell in the grid, and each cell is visited once.

## Space Complexity: O(n * m)
- pacific and atlantic sets store the cells that can flow to the pacific and atlantic oceans respectively.
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 1 and len(heights[0]) == 1:
            return [[0, 0]]
        
        max_row, max_col = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, visited, prev_height):
            out_of_bound = r < 0 or c < 0 or r >= max_row or c >= max_col
            if out_of_bound:
                return

            current = heights[r][c]
            is_visited = (r, c) in visited
            is_uphill = current < prev_height
            if is_visited or is_uphill:
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, current)

        for r in range(max_row):
            dfs(r, 0, pacific, heights[r][0]) # left
            dfs(r, max_col - 1, atlantic, heights[r][max_col - 1]) # right
        for c in range(max_col):
            dfs(0, c, pacific, heights[0][c]) # top
            dfs(max_row - 1, c, atlantic, heights[max_row - 1][c]) # bottom

        return list(pacific & atlantic)
