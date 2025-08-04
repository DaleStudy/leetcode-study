"""
Constraints:
- The input must be a binary string of length 32

<Solution 1>

Time Complexity: O(1)
- 항상 고정된 32비트 문자열에 대해 연산하므로 상수 시간
    
Space Complexity: O(1)
- 32비트 고정 크기의 문자열 연산만 사용하므로 상수 공간

풀이 방법:
1. format(n, '032b')를 사용해 입력받은 정수를 32비트 이진수 문자열로 변환함
2. 문자열 슬라이싱 [::-1]으로 비트를 뒤집음
3. int(reversed_binary, 2)로 뒤집은 이진수 문자열을 다시 정수로 변환함
"""
class Solution:
    def reverseBits(self, n: int) -> int:

        binary = format(n, '032b')

        reversed_binary = binary[::-1]
        
        return int(reversed_binary, 2)

# 코드를 간결하게 정리한 버전
class Solution:
    def reverseBits(self, n: int) -> int:

        return int(format(n, '032b')[::-1], 2)
"""
<Solution 2>

Time Complexity: O(1)
- 각 반복에서 비트 연산은 상수 시간이 걸림

Space Complexity: O(1)
- 사용되는 변수는 result와 입력값 n밖에 없음

풀이 방법:
- ...
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1              # 결과를 왼쪽으로 한 칸 밀고
            result |= n & 1           # n의 마지막 비트를 결과에 추가
            n >>= 1                   # n을 오른쪽으로 한 칸 밀어 다음 비트로 이동
        return result
