class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
        return res

        ## TC: O(m * n), SC: O(m * n)
        ## This sloution is kinda tricky and has higher SC than the below one

        # res = []
        # if len(matrix) == 0:
        #     return res
        # row_begin = 0
        # col_begin = 0
        # row_end = len(matrix)-1
        # col_end = len(matrix[0])-1
        # while (row_begin <= row_end and col_begin <= col_end):
        #     for i in range(col_begin,col_end+1):
        #         res.append(matrix[row_begin][i])
        #     row_begin += 1
        #     for i in range(row_begin,row_end+1):
        #         res.append(matrix[i][col_end])
        #     col_end -= 1
        #     if (row_begin <= row_end):
        #         for i in range(col_end,col_begin-1,-1):
        #             res.append(matrix[row_end][i])
        #         row_end -= 1
        #     if (col_begin <= col_end):
        #         for i in range(row_end,row_begin-1,-1):
        #             res.append(matrix[i][col_begin])
        #         col_begin += 1
        # return res
