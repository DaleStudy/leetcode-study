# Time Complexity: O(m * n) - running DFS from each border, so worst case, we visit each cell twice.
# Space Complexity: O(m * n) - using two sets to track which cells can reach each ocean and the recursion stack.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])
        result = []  
        
        # tracking which cells can reach each ocean
        pac, atl = set(), set() 

        def dfs(r, c, visited, preHeight):
            # if out of bounds, already visited, or can't flow from prev height → just dip
            if (r < 0 or c < 0 or r == rows or c == cols or 
                (r, c) in visited or heights[r][c] < preHeight):
                return

            # mark as visited
            visited.add((r, c))  

            # go in all 4 directions
            dfs(r + 1, c, visited, heights[r][c])  # down
            dfs(r - 1, c, visited, heights[r][c])  # up
            dfs(r, c + 1, visited, heights[r][c])  # right
            dfs(r, c - 1, visited, heights[r][c])  # left

        # hit up all border cells for both oceans
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])  # top row (pacific)
            dfs(rows - 1, c, atl, heights[rows - 1][c])  # bottom row (atlantic)

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])  # leftmost col (pacific)
            dfs(r, cols - 1, atl, heights[r][cols - 1])  # rightmost col (atlantic)

        # now just check which cells are in both sets
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])

        return result
