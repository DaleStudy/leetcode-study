# # 417. Pacific Atlantic Water Flow
from collections import deque

class Solution:
    # Time Complexity O(m*n)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Two BFS 
        # intersection of two hash sets 
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        m, n = len(heights), len(heights[0])
        for j in range(n):
            p_que.append((0,j))
            p_seen.add((0,j))

        for i in range(1,m):
            p_que.append((i,0))
            p_seen.add((i,0))
        
        for i in range(m):
            a_que.append((i, n-1))
            a_seen.add((i, n-1))
        
        for j in range(n-1):
            a_que.append((m-1,j))
            a_seen.add((m-1,j))
        
        def get_coords(que,seen):
            coords = set()
            while que:
                i, j = que.popleft()
                coords.add((i,j))
                for i_off, j_off in [(0,1), (1,0), (-1,0), (0,-1)]:
                    r, c = i+i_off, j +j_off
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))
            return coords
        
        p_coords = get_coords(p_que, p_seen)
        a_coords = get_coords(a_que, a_seen)
        return list(p_coords.intersection(a_coords))

# # First Draft 

# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

#         # first Attempt 
#         self.res = [] 
#         self.pacific = []
#         self.atlantic = []
#         # Brute Force
#         # DFS - every single position 
#         # 1. Pacific Ocean ( in a row: the left side is less than the number) or ( in a column, the previous value is less than the number)
#         # 2. Atlantic Ocean ( in a row: the right side is less than the number) or (in a column, the next values are less than the number)
#         # 3. if the number satisfies both then we add the coordinates of the number to the result 

#         def dfs(list_check):
#             find_max = max(list_check)
#             max_index = list_check.index(find_max)


#             # pacific 
#             if max_index != 0: 
#                 check_paci = [0, max_index]
#                 self.pacific.append(check_paci)
#             if max_index != len(list_check):
#                 check_atlantic = [max_index, 0]
#                 self.atlantic.append(check_atlantic)

#         if len(heights) == 1:
#             return [[0,0]]

#         for i, row in enumerate(heights):

#             dfs(row)
        
#         columns = list(zip(*heights))  # each column becomes a tuple
#         for c, col in enumerate(columns):
#             dfs(col)
#         print(self.pacific)
#         print(self.atlantic)

#         return self.res 

        