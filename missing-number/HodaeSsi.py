class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		n = len(nums)
		expected_sum = (n ** 2 + n) // 2
		
		actual_sum = sum(nums)
		
		return expected_sum - actual_sum

