# 시간 복잡도 : O(nlogn)
# 공간 복잡도 : O(n)
# 문제 유형 : DP, Binary Search
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		dp = []
		for num in nums:
			if not dp or num > dp[-1]:
				dp.append(num)
			else:
				left, right = 0, len(dp) - 1
				while left < right:
					mid = left + (right - left) // 2
					if dp[mid] < num:
						left = mid + 1
					else:
						right = mid
				dp[right] = num
		return len(dp)

