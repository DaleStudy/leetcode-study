"""
Constraints:
- 1 <= n <= 2^31 - 1

Time Complexity: O(k)
- 여기서 k는 입력의 비트 수
- 이 경우 32비트 정수이므로 실질적으로 O(1) (항상 최대 32번 반복하기 때문)

Space Complexity: O(1)
- count 변수만 사용하므로 상수 공간 복잡도
"""
class Solution:
   def hammingWeight(self, n: int) -> int:
       count = 0
       while n:
           count += n & 1  # 현재 마지막 비트가 1인지 확인
           n >>= 1        # 다음 비트 검사를 위해 오른쪽 시프트
       return count
