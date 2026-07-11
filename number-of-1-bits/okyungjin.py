# https://leetcode.com/problems/number-of-1-bits/description/

# n을 2진법으로 변환했을 때 1의 개수를 세는 문제이다.
# `n & 1` 연산을 통해 마지막 비트가 1인지 검사해서 count를 증가시킨다.
# 확인한 비트를 `n >>= 1` 으로 한자리 버린다.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            # `n & 1` 연산을 통해 마지막 비트가 1인지 검사해서 count를 증가시킨다.

            #   1011
            # & 0001
            # ------
            # 0001 -> 결과 1이 된다
            count += n & 1

            # 비트 한자리 이동한다 (1011 -> 0101)
            n = n >> 1

        return count
