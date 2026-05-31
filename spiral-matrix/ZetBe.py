'''
문제: 나선형으로 행렬을 순회하며 모든 원소를 반환
풀이: 방문한 위치를 기록하는 행렬을 만들어 현재 방향으로 이동할 수 있는지 확인하며 이동, 이동할 수 없으면 방향을 바꿈
시간복잡도: O(m*n) (m: 행의 수, n: 열의 수)
공간복잡도: O(m*n) (방문 기록을 위한 행렬)
사용한 자료구조: 리스트
개인적인 회고: 문제 자체는 단순하지만 경계 조건과 방향 전환 로직을 꼼꼼히 처리해야 해서 구현에 신경을 써야 했다. 방문 기록 행렬을 사용하여 이미 방문한 위치를 피하는 방식이 직관적이고 이해하기 쉬웠다.
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        v = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        if len(v) == 1:
            return [i for i in matrix[0]]
        if len(v[0]) == 1:
            answer = []
            for i in matrix:
                for j in i:
                    answer.append(j)
            return answer
        answer = []
        d = [[0, 1], [1, 0], [0, -1],  [-1, 0]]
        i = 0
        y, x = 0, 0
        while True:
            if len(answer) == len(v)*len(v[0]):
                break
            v[y][x] = 1
            answer.append(matrix[y][x])
            ny = y + d[i][0]
            nx = x + d[i][1]
            if not(0 <= nx < len(v[0]) and 0 <= ny < len(v) and v[ny][nx] == 0):
                i = (i+1)%4
                ny, nx = y + d[i][0], x + d[i][1]
            y, x = ny, nx
            

        return answer
                

