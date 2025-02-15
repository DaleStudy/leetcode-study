"""
	풀이 : 
		해당 인덱스의 숫자로 끝나는 LIS의 길이를 dp배열에 저장
		nums[i] 와 그 이후에 오는 nums[j]를 비교해 nums[j]가 크고 
		i까지의 LIS 길이 + 1 > j까지의 LIS길이이면 j까지의 LIS길이 업데이트
		업데이트 할 때마다 max길이와 비교해서 최대길이 업데이트

	nums의 길이 N
	TC : O(N^2)
		for문의 개수를 살펴보면 N-1 + N-2 + ... + 1 = (N-1)N/2 이므로 N^2/2 -> O(N^2)

	SC : O(N)
		dp의 길이는 nums의 길이에 비례하므로
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        max_LIS = 1
        for i in range(len(nums) - 1) :
            for j in range(i + 1, len(nums)) :
                if nums[i] < nums[j] and dp[i] + 1 > dp[j] :
                    dp[j] = dp[i] + 1
                    max_LIS = max(max_LIS, dp[j])
        return max_LIS
