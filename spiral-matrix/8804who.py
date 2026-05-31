class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []

        y_s, y_e = 0, len(matrix)-1
        x_s, x_e = 0, len(matrix[0])-1

        while y_s <= y_e and x_s <= x_e:
            for i in range(x_s, x_e+1):
                answer.append(matrix[y_s][i])
            for i in range(y_s+1, y_e+1):
                answer.append(matrix[i][x_e])

            if y_s==y_e or x_s==x_e:
                break

            for i in range(x_e-1, x_s-1, -1):
                answer.append(matrix[y_e][i])
            for i in range(y_e-1, y_s, -1):
                answer.append(matrix[i][x_s])

            y_s, y_e = y_s+1, y_e-1
            x_s, x_e = x_s+1, x_e-1
        
        return answer
    
