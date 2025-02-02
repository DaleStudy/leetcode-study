"""
    풀이 : mask를 int 비트 수 만큼 이동시키면서 1의 개수 센다

    TC : O(1)

    SC : O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1 << 31
        cnt = 0
        while mask :
            if mask & n :
                cnt += 1
            mask >>= 1
        return cnt
