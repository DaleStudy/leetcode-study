"""
Solution: 해설을 활용한 풀이입니다.
    1) xor 로 더하기를 만들 수있다. 
    2) & << 1 로 carry 를 만들 수 있다.
    3) python 의 경우 32비트 마스크를 사용해 음수 케이스를 고려한다.

"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        xor = a ^ b
        carry = (a & b) << 1
        while carry & mask:
            xor, carry = xor ^ carry, (xor & carry) << 1
        return (xor & mask) if carry > 0 else xor
