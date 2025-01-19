# 공간 복잡도: O(n) => nums 길이만큼 dp 배열 길이만큼의 공간 사용
# 시간 복잡도: O(n^2) => 외부 반복문은 O(N), 내부 반복문은 O(N) 시간이 소요되므로 총 O(N*N) = O(N^2) 소요
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for cur in range(1, len(nums)):
            for prev in range(cur):
                if nums[cur] > nums[prev]:
                    dp[cur] = max(dp[prev]+1, dp[cur])
        
        return max(dp)
