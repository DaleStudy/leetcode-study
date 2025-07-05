"""
정수 n이 주어졌을 때, 0부터 n까지의 모든 수에 대해 각 수를 이진수로 표현했을 때 1의 개수를 구하는 문제

TC: O(N log N), 모든 수 순환 + 이진수 변환 과정 (log i)
SC: O(N)
"""

from typing import List

# 처음 풀이
class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOne(num):
            cnt = 0
            while True:
                rest = num % 2
                if rest == 1:
                    cnt += 1
                num //= 2
                if num <= 1:
                    if num == 1:
                        cnt += 1
                    break
            return cnt

        result = []
        for i in range(0, n + 1):
            result.append(countOne(i))

        return result
    
"""
DP 풀이 - 시간 복잡도 개선

bits[i] = bits[i >> 1] + (i &)
i >> 1 은 i를 오른쪽으로 1비트 이동 -> i를 2로 나눈 값
i & 1 은 i의 마지막 1비트가 1인지 확인, 짝수면 0, 홀수면 1
i의 1의 개수 = i를 2로 나눈 수의 1의 개수 + 마지막 비트가 1인지 여부

TC: O(N)
SC: O(N)
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
