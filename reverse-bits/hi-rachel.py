"""
1. 입력받은 정수 n을 32비트 이진수로 바꾼다
2. 이진수를 좌우로 뒤집는다 -> stack 활용
2. 뒤집은 이진수의 정수값을 반환한다

항상 32비트이므로 상수 시간, 상수 공간
TC: O(1)
SC: O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        stack = []
        while len(stack) < 32:
            stack.append(n % 2)
            n //= 2

        output, scale = 0, 1  # 결과, 2^0 = 1 시작
        while stack:
            output += stack.pop() * scale
            scale *= 2

        return output

"""
비트 연산자

쉬프트 연산자 - 정수 타입에만 사용 가능, 내부적으로 이진수로 작동
<< 비트를 왼쪽으로 이동
x << 1 == x * 2
ex) 00001101 → 00011010

>> 비트를 오른쪽으로 이동
x >> 1 == x // 2
ex) 00001101 → 00000110

n & 1
현재 n의 가장 오른쪽 비트 확인
n & 1이 1이면 홀수, 0이면 짝수
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        stack = []
        while len(stack) < 32:
            stack.append(n & 1)  # 마지막 비트 1이면 1, 0이면 0
            n >>= 1  # %= 2 와 같은 효과, 오른쪽 쉬프트

        output, scale = 0, 1  # 결과, 2^0 = 1 시작
        while stack:
            output += stack.pop() * scale
            scale <<= 1  # *= 2 와 같은 효과

        return output

# stack 공간 절약 풀이
class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for _ in range(32):
            output <<= 1  # 왼쪽 쉬프트
            output |= (n & 1)  # 논리 연산자 사용 (제일 마지막 비트가 1이라면 1, 0이라면 0)
            n >>= 1
        return output

# int, format 활용 풀이
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(format(n, "032b")[::-1], 2)
