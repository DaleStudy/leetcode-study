"""
https://leetcode.com/problems/house-robber/description/

시간 복잡도: O(n)
- 모든 배열 한 번씩 순회 O(n)
- 선택/미선택 값 비교 O(1)

공간 복잡도: O(n)
- 각 인덱스까지의 최대 금액 dp 배열에 저장

점화식:
- dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
- nums[i] + dp[i - 2]: 현재 집을 터는 경우
- dp[i - 1]: 현재 집을 털지 않는 경우
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[-1]
