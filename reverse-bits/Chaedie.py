"""
1. 학습은 진행했지만, 스스로 완벽하게 풀지 못했습니다.
    다음주에 bit 연산으로 다시 풀어볼 예정입니다.
"""


class Solution:

    # 알고달레 풀이 1) Stack
    def reverseBits(self, n: int) -> int:
        stack = []
        while len(stack) < 32:
            stack.append(n % 2)
            n //= 2

        result, scale = 0, 1
        while stack:
            result += stack.pop() * scale
            scale *= 2
        return result

    # 알고달레 풀이 2) bit manipulation
    def reverseBits(self, n: int) -> int:
        result = 0
        print(n)
        for i in range(32):
            print(result)
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

    # NeetCode 풀이
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res

    # 스스로 풀기
    # 한번 더 풀 에정입니다.
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = result << 1
            result = result | (n & 1)
            n = n >> 1
        return result
