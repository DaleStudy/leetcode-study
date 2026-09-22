# TC: O(N*M)
# SC: O(N*M)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        n = len(heights)
        m = len(heights[0])

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col, check):
            check[row][col] = True

            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]

                if 0 <= new_row < n and 0 <= new_col < m and not check[new_row][new_col] and heights[row][col] <= heights[new_row][new_col]:
                    dfs(new_row, new_col, check)

        pac_check = [[False for _ in range(m)] for _ in range(n)]
        atl_check = [[False for _ in range(m)] for _ in range(n)]

        for row in range(1, n):
            dfs(row, 0, pac_check)

        for col in range(m):
            dfs(0, col, pac_check)

        for row in range(n - 1):
            dfs(row, m - 1, atl_check)

        for col in range(m):
            dfs(n - 1, col, atl_check)

        ans = []

        for row in range(n):
            for col in range(m):
                if pac_check[row][col] and atl_check[row][col]:
                    ans.append([row, col])

        return ans

