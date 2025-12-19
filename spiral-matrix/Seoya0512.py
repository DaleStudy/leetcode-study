'''
해당 문제를 확인하고 
상단 -> 우측 -> 하단 -> 좌측 방향으로 나선형으로 접근하는 것을 우선순위로 생각했습니다.
pop을 통해서 matrix의 행과 열을 제거하면서 접근하는 방식을 사용해 해결했습니다.

이렇게 문제를 풀었을때 pop을 사용하여 행과 열을 제거하기 때문에 
비싼 계산 비용이 발생하는 부분을 고려하지 못했다는 점이 아쉽게 느껴지네요. 

Time Complexity: O(mxn)
- m: 행의 수만큼 접근
- n: 열의 수만큼 접근

Space Complexity: O(mxn)
- result 리스트가 전체 요소를 저장
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        idx = 0 # 처음 값
        while matrix:
            result += matrix.pop(idx)
            for i in range(len(matrix)):
                if matrix[i]:
                    result.append(matrix[i].pop())

            # 빈 행 제거 (중요!)
            matrix = [row for row in matrix if row]
            if not matrix:
                break

            result += matrix.pop()[::-1]

            for j in range(len(matrix)-1, -1, -1):
                if matrix[j]:
                    result.append(matrix[j].pop(0))

        return result

