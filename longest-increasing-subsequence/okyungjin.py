"""
https://leetcode.com/problems/longest-increasing-subsequence/

정수 배열 nums가 주어졌을 때, 가장 긴 증가하는 부분수열(연속하지 않아도 됨)의 길이를 구한다.

1. `dp[i]`:  `nums[i]`로 끝나는 증가 부분수열 중 최장 길이
2. 모든 i에 대해, i보다 앞에 있고 값이 더 작은 j들의 dp[j] 중 최댓값 + 1을 dp[i]에 저장한다.
3. 답은 dp 배열 전체의 최댓값이다.

Time: O(n^2)
Space: O(n)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1

        return max(dp)

# TODO: O(n log n)으로 최적화 필요
