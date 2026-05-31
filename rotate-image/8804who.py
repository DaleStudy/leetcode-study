from collections import deque

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def sub(s, e):
            q = deque()

            for i in range(s, e+1):
                q.append(matrix[s][i])
            for i in range(s+1, e+1):
                q.append(matrix[i][e])
            for i in range(e-1, s-1, -1):
                q.append(matrix[e][i])
            for i in range(e-1, s, -1):
                q.append(matrix[i][s])

            for _ in range(e-s):
                q.appendleft(q.pop())
            
            for i in range(s, e+1):
                matrix[s][i] = q.popleft()
            for i in range(s+1, e+1):
                matrix[i][e] = q.popleft()
            for i in range(e-1, s-1, -1):
                matrix[e][i] = q.popleft()
            for i in range(e-1, s, -1):
                matrix[i][s] = q.popleft()

            if s+1 <= e-1:
                sub(s+1, e-1)

        sub(0, len(matrix)-1)
    
