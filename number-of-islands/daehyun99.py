# Time: O(M * N)
# Space: O(M * N)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h = len(grid)
        w = len(grid[0])
        count = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    stack = []
                    stack.append([i, j])
                    while len(stack) > 0 :
                        x, y = stack.pop()

                        grid[x][y] = "0"
                        if x > 0 and grid[x-1][y] == "1":
                            stack.append([x-1, y])
                        if x + 1 < h and grid[x+1][y] == "1":
                            stack.append([x+1, y])
                        if y > 0 and grid[x][y-1] == "1":
                            stack.append([x, y-1])
                        if y + 1 < w and grid[x][y+1] == "1":
                            stack.append([x, y+1])
                    count += 1
        return count
