# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def check(matrix, matrix_seen):
            while len(matrix) > 0:
                m,n = matrix.pop()
                if m+1 < len(heights) and heights[m][n] <= heights[m+1][n] and (m+1,n) not in matrix_seen:
                    matrix.add((m+1,n))
                    matrix_seen.add((m+1,n))
                if m-1 >= 0 and heights[m][n] <= heights[m-1][n] and (m-1,n) not in matrix_seen:
                    matrix.add((m-1,n))
                    matrix_seen.add((m-1,n))
                if n+1 < len(heights[0]) and heights[m][n] <= heights[m][n+1] and (m,n+1) not in matrix_seen:
                    matrix.add((m,n+1))
                    matrix_seen.add((m,n+1))
                if n-1 >= 0 and heights[m][n] <= heights[m][n-1] and (m,n-1) not in matrix_seen:
                    matrix.add((m,n-1))
                    matrix_seen.add((m,n-1))
            return matrix_seen

        pacific = set()
        pacific_seen = set()
        for i in range(len(heights[0])):
            pacific.add((0, i))
            pacific_seen.add((0, i))
        for i in range(1, len(heights)):
            pacific.add((i, 0))
            pacific_seen.add((i, 0))
        
        p_seen = check(pacific, pacific_seen)

        atlantic = set()
        atlantic_seen = set()
        for i in range(len(heights[0])):
            atlantic.add((len(heights)-1, i))
            atlantic_seen.add((len(heights)-1, i))
        for i in range(0, len(heights)):
            atlantic.add((i, len(heights[0])-1))
            atlantic_seen.add((i, len(heights[0])-1))
    
        a_seen = check(atlantic, atlantic_seen)

        result = []
        for p in p_seen:
            if p in a_seen:
                result.append(list(p))
        return result

