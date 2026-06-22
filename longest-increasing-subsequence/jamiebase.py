"""
# Approach
dp[n]은 nums[n] 위치까지 lis 길이입니다.

# Complexity
nums의 길이를 n이라고 할 때,
- Time complexity: 이중 반복문 O(N^2)
- Space complexity: dp 배열 O(N)
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n
        answer = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
            answer = max(answer, dp[i])
        return answer
