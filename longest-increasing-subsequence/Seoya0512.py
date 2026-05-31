'''
Dynamic Programming 문제로 누적합을 이용해 풀어보려 했으나 끝내 해결을 못해 참고했습니다. 
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for cur in range(1, len(nums)):
            for prev in range(len(nums)):
                if nums[prev] < nums[cur]:
                    dp[cur] = max(1+dp[prev], dp[cur])
        return max(dp)

