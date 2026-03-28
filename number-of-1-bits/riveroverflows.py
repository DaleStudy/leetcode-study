from typing import *


class Solution:
    """
    TC: O(log n)
    SC: O(1)

    풀이:
    Brian Kernighan의 비트 트릭을 활용.
    n & (n-1)은 n의 가장 오른쪽 1비트를 하나 제거한다.
    n이 0이 될 때까지 반복한 횟수가 곧 1비트의 개수.
    """
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n > 0:
            n = n & (n - 1)
            answer += 1

        return answer
