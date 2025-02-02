"""
Solution: 
    1) 숫자에 1 bit 을 and 연산 결과가 1일 경우 result 에 1을 더한다.
    2) n 을 오른쪽으로 쉬프팅 시킨다.

N: n의 bit 수
Time: O(N)
Space: O(1)

"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n > 0:
            if n & 1:
                result += 1
            n = n >> 1
        return result
