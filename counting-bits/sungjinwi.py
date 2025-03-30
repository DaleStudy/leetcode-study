"""
    풀이 :
        가장 낮은 자리의 비트를 제외한 dp의 성분 + 가장 낮은 자리 비트를 통해 dp 구현
    
    n의 크기 : N

    TC : O(N)

    SC : O(N)
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for num in range(1, n + 1):
            dp[num] = dp[num >> 1] + (num & 1)

        return dp
