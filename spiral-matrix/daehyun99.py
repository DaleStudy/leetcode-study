class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        weight = len(matrix[0])
        adding = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        m = 0
        n = -1
        size = height * weight
        count = 0

        result = []
        
        while count < size:
            if 0 < weight and count < size:
                m_add, n_add = adding[0]
                for _ in range(weight):
                    m += m_add
                    n += n_add
                    result.append(matrix[m][n])
                    count += 1

            height -= 1
            if 0 < height and count < size:
                m_add, n_add = adding[1]
                for _ in range(height):
                    m += m_add
                    n += n_add
                    result.append(matrix[m][n])
                    count += 1

            weight -= 1
            if 0 < weight and count < size:
                m_add, n_add = adding[2]
                for _ in range(weight):
                    m += m_add
                    n += n_add
                    result.append(matrix[m][n])
                    count += 1
            
            height -= 1
            if 0 < height and count < size:
                m_add, n_add = adding[3]
                for _ in range(height):
                    m += m_add
                    n += n_add
                    result.append(matrix[m][n])
                    count += 1

            weight -= 1
        return result
