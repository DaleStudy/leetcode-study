# https://leetcode.com/problems/counting-bits/

from typing import List

class Solution:
    def countBits1(self, n: int) -> List[int]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            다음과 같은 규칙을 찾을 수 있다.

            0 ~ 1   bin(0) = 0
                    bin(1) = 1

            2 ~ 3   bin(2) = 10 = 10 + bin(0)
                    bin(3) = 11 = 10 + bin(1)
                    => offset = 10(2) = 2 (-> 1이 1개)

            4 ~ 7   bin(4) = 100 = 100 + bin(0)
                    bin(5) = 101 = 100 + bin(1)
                    bin(6) = 110 = 100 + bin(2)
                    bin(7) = 111 = 100 + bin(3)
                    => offset = 100(2) = 4 (-> 1이 1개)

            8 ~ 15  bin(8) = 1000 = 1000 + bin(0)
                    ...
                    bin(15) = 1111 = 1000 + bin(7)
                    => offset = 1000(2) = 8 (-> 1이 1개)
        """

        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            # i가 2의 제곱이면, offset 2배
            if offset * 2 == i:
                offset *= 2

            # 이전에 구한 값 사용
            dp[i] = dp[i - offset] + 1

        return dp

    def countBits(self, n: int) -> List[int]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)
        """

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # dp[i] = dp[i // 2] + (i % 2)
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
