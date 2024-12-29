#시간복잡도 : O(n^2), 공간복잡도 : O(1)

class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		for i in range(len(nums) - 1):
			for k in range(i + 1, len(nums)):
				if (nums[i] + nums[k] == target):
					return ([i, k])

