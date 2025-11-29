# 문제 풀이
# 1. 입력값 n을 binary 형태로 변환
#   - 입력값 n이 1보다 크면 2로 나눠 몫과 나머지 계산
#   - 나머지를 리스트에 추가해 반환
# 2. 반환된 리스트에서 1의 갯수 반환

# 시간복잡도 O(log n): n을 2로 나누면서 재귀 함수 실행
# 공간복잡도 O(log n): 비트를 저장하는 리스트의 길이

class Solution:
    def devide_by_2 (self, n, temp):
        if n > 1 :
            temp.append(n % 2)
            return self.devide_by_2(n // 2, temp)
        temp.append(1)
        return n, temp

    def hammingWeight(self, n: int) -> int:
        result = []
        n, result = self.devide_by_2(n, result)
        return result.count(1)